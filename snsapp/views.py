from django.shortcuts import render
from django.contrib.auth.models import User  # Userモデルをimport
from django.db import IntegrityError  # IntegrityErrorの表示のために

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

    return render(request, 'signup.html', {'some': 100})
