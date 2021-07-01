from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Userモデルをimport
from django.contrib.auth import authenticate, login  # ログインのために
from django.db import IntegrityError  # IntegrityErrorの表示のために
from .models import SnsModel
from django.contrib.auth.decorators import login_required
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
    return render(request, 'login.html', {'context': 'get method'})


# @login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})

