from django.urls import path
from . import views

app_name = 'net_a'
urlpatterns = [
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
    path('fish_info', views.fish_info, name='fish_info'),
    path('favorite', views.favorite, name='favorite'),
    path('edit_fish_check', views.edit_fish_check, name='edit_fish_check'),
    path('edit_fish', views.edit_fish, name='edit_fish'),
    path('base', views.base, name='base'),
    path('add_fish_check', views.add_fish_check, name='add_fish_check'),
    path('add_fish', views.add_fish, name='add_fish')
]

"""my_pageへのURL設定↑（1行）"""

"""
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]

URL configuration for net_a project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""