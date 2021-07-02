from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User  # Userモデルをimport
from django.contrib.auth import authenticate, login, logout  # ログインのために
from django.db import IntegrityError  # IntegrityErrorの表示のために
from .models import SnsModel
# from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.


def signupfunc(request):
    # POSTだった場合の挙動
    if request.method == 'POST':
        # POSTで送られてきている各項目の内容を、変数に代入する
        username = request.POST['username']
        password = request.POST['password']
        try:
            # 上で取得した内容で新規ユーザーを作成する。このコマンドが実行された時点でユーザーが作成される。
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(
                request, 'signup.html', {'error': 'このユーザーはすでに登録されています'}
                )

    # GETの場合の挙動
    return render(request, 'signup.html', {'': ''})


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 取得したデータから、オーソリをかける
        user = authenticate(request, username=username, password=password)
        # ユーザーがデータベースに存在していたら
        if user is not None:
            # ログインさせる
            login(request, user)
            return redirect('list')
        else:
            return render(
                request, 'login.html', {'context': '正しい情報でログインしてください'}
                )
    # GETの場合の挙動
    return render(request, 'login.html', {'context': 'GETでアクセス'})


# @login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    object_list = reversed(object_list)
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):  # URLに付け加えられる数字の情報を引数で受ける
    # 対象のオブジェクトがあればオブジェクトを返すし、なければ404エラーを返してくれるdjangoのメソッド
    # get_object_or_404(klass, *args, **kwargs)  klass:modelクラス pkを指定
    detail_object = get_object_or_404(SnsModel, pk=pk)
    # Calls get() on a given model manager, but it raises Http404 instead of the model's DoesNotExist exception.
    # klass
    # A Model class, a Manager, or a QuerySet instance from which to get the object.
    # **kwargs
    # Lookup parameters, which should be in the format accepted by get() and filter().

    # user_object = SnsModel.object.get('')  # この書き方でも良い
    return render(request, 'detail.html', {'detail_object': detail_object})


def goodfunc(request, pk):
    # プライマリーキーでモデルからオブジェクトを取得する
    detail_object = SnsModel.objects.get(pk=pk)
    # オブジェクトのgood属性（フィールド）にプラス１する
    detail_object.good += 1
    # オブジェクトのデータを保存する
    detail_object.save()
    return redirect('list')


# 本番環境ではなく開発環境で動かすための実装
# 既読ボタンをおす->ユーザーが既読をした人であれば、何もしない、既読をしていない人であれば既読フィールドにプラスして、既読ユーザーリストに名前を加える
def readfunc(request, pk):
    detail_object = SnsModel.objects.get(pk=pk)
    # requestオブジェクトからログインしているユーザー名を取得する
    username = request.user.get_username()
    if username in detail_object.read_text:  # SnsModelのread_textフィールドに名前があったら
        return redirect('list')
    else:
        detail_object.read += 1
        # 既読を管理しているread_textに名前を追加　本番には非現実的だが。
        detail_object.read_text = detail_object.read_text + ' ' + username
        detail_object.save()
        return redirect('list')


class SnsCreate(CreateView):
    template_name = 'create.html'
    model = SnsModel
    fields = ('title', 'content', 'author', 'sns_image')
    success_url = reverse_lazy('list')
