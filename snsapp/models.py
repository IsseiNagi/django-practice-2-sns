from django.db import models

# Create your models here.


class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    # 画像をアップロードした保存先。引数は必須
    # ImageFieldを使うためにはPillowをインストールしないといけない
    sns_image = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    # 既読した数を管理するため。同じユーザーの場合は既読数がカウントアップされない。
    read_text = models.TextField(null=True, blank=True, default='author')

    # null=True：データベースに空の内容が入ってきても許可する
    # blank=True：フォームで入力されていなくても許可する
