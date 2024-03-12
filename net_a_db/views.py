from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def sign_up_check(request):
    return render(request, 'sign_up_check.html')
def sign_up(request):
    return render(request, 'sign_up.html')
def sign_in(request):
    return render(request, 'sign_in.html')
def setting(request):
    return render(request, 'setting.html')
def search(request):
    return render(request, 'search.html')
def privacy(request):
    return render(request, 'privacy.html')
def net_a_tutorial(request):
    return render(request, 'net_a_tutorial.html')
def my_page(request):
    return render(request, 'my_page.html')
def my_fish(request):
    return render(request, 'my_fish.html')
def index(request):
    return render(request, 'index.html')
def history(request):
    return render(request, 'history.html')
def genre_list(request):
    return render(request, 'genre_list.html')
def fish_info(request):
    return render(request, 'fish_info.html')
def favorite(request):
    return render(request, 'favorite.html')
def edit_fish_check(request):
    return render(request, 'edit_fish_check.html')
def edit_fish(request):
    return render(request, 'edit_fish.html')
def base(request):
    return render(request, 'base.html')
def add_fish_check(request):
    return render(request, 'add_fish_check.html')
def add_fish(request):
    return render(request, 'add_fish.html')
def registration(request):
    return render(request, 'registration.html')
def base_root(request):
    return render(request, 'base_root.html')


from net_a_db.forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    user_form = UserForm(request.POST or None)
    #profile_form = ProfileForm(request.POST or None, request.FILES or None)
    if user_form.is_valid():
        user = user_form.save(commit=False)# 一時的に保存を遅らせる
        password = user_form.cleaned_data.get('password')# パスワードを取得
        user.set_password(password)# パスワードをハッシュ化して設定
        user.save()# ハッシュ化されたパスワードを持つユーザーを保存
        """
        条件式に追加and profile_form.is_valid()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()"""
    return render(request, 'registration.html', context={
        'user_form': user_form,
        #'profile_form': profile_form,
    })

def user_login(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        #ユーザーが存在するか、パスワードがあっているか
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('アカウントがアクティブでないです')
        else:
            return HttpResponse('ユーザーが存在しません')
    return render(request, 'login.html', context={
        'login_form': login_form
    })

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def info(request):
    return HttpResponse('ログインしています')

from .models import FishInfo


def index(request):
    fish_infos = FishInfo.objects.all()  # すべての FishInfo レコードを取得
    return render(request, 'index.html', {'fish_infos': fish_infos})

def fish_info(request, fish_info_id):
    fish_info = get_object_or_404(FishInfo, pk=fish_info_id)
    return render(request, 'fish_info.html', {'fish_info': fish_info})

"""
from .models import FishInfo
def fish_info(request):
    fish_infos = FishInfo.objects.filter(id=1).all()  # すべての FishInfo レコードを取得
    return render(request, 'fish_info.html', {'fish_infos': fish_infos})
"""
"""
オブジェクト化したい
for page in pages:
    def index(request):
        return render(request, str(page) + '.html')
        

"""