from django.db import models

# Create your models here.


class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    # 画像をアップロードした保存先。引数は必須
    # ImageFieldを使うためにはPillowをインストールしないといけない
    sns_image = models.ImageField(upload_to='')
    good = models.IntegerField()
    read = models.IntegerField()
    # 既読した数を管理するため。同じユーザーの場合は既読数がカウントアップされない。
    read_text = models.TextField()
