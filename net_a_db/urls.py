from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up_check', views.sign_up_check, name='sign_up_check'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('setting', views.setting, name='setting'),
    path('search', views.search, name='search'),
    path('privacy', views.privacy, name='privacy'),
    path('net_a_tutorial', views.net_a_tutorial, name='net_a_tutorial'),
    path('my_page/', views.my_page, name='my_page'),
    path('my_fish', views.my_fish, name='my_fish'),
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('genre_list', views.genre_list, name='genre_list'),
    path('fish_info', views.fish_info, name='fish_info'),
    path('favorite', views.favorite, name='favorite'),
    path('edit_fish_check', views.edit_fish_check, name='edit_fish_check'),
    path('edit_fish', views.edit_fish, name='edit_fish'),
    path('base', views.base, name='base'),
    path('add_fish_check', views.add_fish_check, name='add_fish_check'),
    path('add_fish', views.add_fish, name='add_fish'),
    path('registration', views.registration, name='registration'),
    path('base_root', views.base_root, name='base_root'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('info', views.info, name='info'),
]
