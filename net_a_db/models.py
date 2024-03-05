from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.FileField(upload_to='user/', blank=True)

    def __str__(self):
        return self.user.username

#テーブル定義
class User(models.Model):
    icon_id = models.ForeignKey(
        'icon', default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=254, db_index=True)
    password = models.CharField(max_length=128)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class FishInfo(models.Model):
    user_id = models.ForeignKey(
        'user', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    movie = models.FileField(upload_to='upload_video/')
    info = models.TextField(max_length=1000)
    gender = models.IntegerField(blank=True)
    fish_mixed = models.CharField(max_length=200)
    temp = models.IntegerField(blank=True)
    fish_size = models.IntegerField(blank=True)
    aquarium_size = models.IntegerField(blank=True)
    material = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class Favorite(models.Model):
    user_id = models.ForeignKey(
        'user', on_delete=models.CASCADE)
    fish_id = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)


class History(models.Model):
    user_id = models.ForeignKey(
        'user', on_delete=models.CASCADE)
    fish_id = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class Icon(models.Model):
    icon_file_name = models.ImageField(upload_to='icon_img/')
    icon_name = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=200, blank=True)#iconに新しくテキストを追加
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class FishPhoto(models.Model):
    fish_info_id = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    fish_file_name = models.ImageField(upload_to='upload_img/')
    display_number = models.IntegerField()
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

"""
ER図通りのIconの設定


class Icon(models.Model):
    icon_file_name = models.ImageField(upload_to='icon_img/')
    icon_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

"""
"""
Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Sales(models.Model):
    fee = models.IntegerField()
"""