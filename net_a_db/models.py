from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ForeignKey(
        'icon', default=1, on_delete=models.SET_DEFAULT)
    website = models.URLField(null=True, blank=True)
    picture = models.FileField(upload_to='user/', null=True, blank=True)

    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    icon = models.ForeignKey('Icon', default=1, on_delete=models.SET_DEFAULT)
    # アイコンへの参照を追加
    """icon = models.ForeignKey('icon', default=1, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username"""

#テーブル定義
class UserInfo(models.Model):
    icon = models.ForeignKey(
        'icon', default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=254, db_index=True)
    password = models.CharField(max_length=128)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class FishInfo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    #previewのカラムを追加
    preview = models.ImageField(upload_to='upload_img/', null=True, blank=True)
    movie = models.FileField(upload_to='upload_video/', null=True, blank=True)
    info = models.TextField(max_length=1000, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    #categoryのカラムを追加
    category = models.CharField(max_length=20, null=True, blank=True)
    fish_mixed = models.CharField(max_length=200, null=True, blank=True)
    temp = models.CharField(max_length=20, null=True, blank=True)
    fish_size = models.IntegerField(null=True, blank=True)
    aquarium_size = models.CharField(max_length=20, null=True, blank=True)
    material = models.CharField(max_length=200, null=True, blank=True)
    food = models.CharField(max_length=200, null=True, blank=True)
    #goodのカラムを追加
    good = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    fish = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)
    #Metaクラスを追加
    class Meta:
        unique_together = ('user', 'fish') 


class History(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    fish = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class Icon(models.Model):
    icon_file_name = models.ImageField(upload_to='icon_img/')
    icon_name = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=200, null=True, blank=True)#iconに新しくテキストを追加
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class FishPhoto(models.Model):
    fish_info = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE, default=1)
    fish_file_name = models.ImageField(upload_to='upload_img/')
    display_number = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

#下記テーブルの追加、ユーザー情報にIcon情報を入れられないため
class Icon_items(models.Model):
    icon = models.ForeignKey(
        'icon', on_delete=models.CASCADE)
    fish_info = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    icon_set = models.IntegerField(default=0, null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)
"""
アップデートに伴う、アイコンの所持情報テーブル
from django.conf import settings

class UserIcon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    obtained_at = models.DateTimeField(auto_now_add=True)  # アイコンを取得した日時
    is_active = models.BooleanField(default=False)  # このアイコンが現在選択されているか

    class Meta:
        unique_together = ('user', 'icon')  # 同じアイコンを複数持たないようにする
"""

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