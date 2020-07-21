# /home/tarena/filmsite/filmsite/user/models.py
from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32, unique=True)
    password = models.CharField(verbose_name="密码", max_length=32)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)


class FilmInfo(models.Model):
    filmname = models.CharField(verbose_name="电影名称", max_length=64)
    filmintro = models.TextField(verbose_name="电影介绍")
    filmlink = models.TextField(verbose_name="电影链接")
    actors = models.TextField(verbose_name="演员名字")
    category = models.TextField(verbose_name="电影类型")
    img = models.TextField(verbose_name="图片链接")
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)


class MessageBoard(models.Model):
    content = models.TextField(verbose_name="留言内容")
    like = models.BooleanField(verbose_name="点赞", default=0)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    film = models.ForeignKey("FilmInfo", on_delete=models.CASCADE)


class Comments(models.Model):
    content = models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)


class History(models.Model):
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    film = models.ForeignKey("FilmInfo", on_delete=models.CASCADE)
