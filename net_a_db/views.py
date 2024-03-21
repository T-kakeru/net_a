from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def tag_list(request):
    return render(request, 'tag_list.html')
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
def favorite_list(request):
    return render(request, 'favorite_list.html')
def fish_info(request):
    return render(request, 'fish_info.html')
def edit_fish_check(request):
    return render(request, 'edit_fish_check.html')
def edit_fish(request):
    return render(request, 'edit_fish.html')
def base(request):
    return render(request, 'base.html')
def add_fish_check(request):
    return render(request, 'add_fish_check.html')
def registration(request):
    return render(request, 'registration.html')
def base_root(request):
    return render(request, 'base_root.html')


from net_a_db.forms import UserForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#新規登録
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)  # ユーザーをログインさせる
            return redirect('net_a_tutorial')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'registration.html', {'user_form': user_form, 'profile_form': profile_form})

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


from .forms import FishInfoForm
from .models import FishInfo, Profile

def add_fish(request):
        fish_info_form = FishInfoForm(request.POST, request.FILES)
        if fish_info_form.is_valid():
            fish_info_form.save()
            return redirect('my_page')

        return render(request, 'add_fish.html', {'fish_info_form': fish_info_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def info(request):
    return HttpResponse('ログインしています')

#indexの色々な情報を表示
def index(request):
    fish_infos = FishInfo.objects.order_by('-create_at')
    fish_infos_size = FishInfo.objects.filter(fish_size__gte=23).order_by('-create_at').all()
    fish_infos_favorites = FishInfo.objects.order_by('-good')
    return render(request, 'index.html', {
        'fish_infos': fish_infos,
        'fish_infos_size': fish_infos_size,
        'fish_infos_favorites': fish_infos_favorites,
        })

#下記、もっと見る[最新の投稿、大きい魚、人気の魚]
def fish_new_list(request):
    fish_new_list = FishInfo.objects.order_by('-create_at')
    return render(request, 'fish_new_list.html', {'fish_new_list': fish_new_list})

def fish_size_list(request):
    fish_size_list = FishInfo.objects.filter(fish_size__gte=23).order_by('-create_at').all()
    return render(request, 'fish_size_list.html', {'fish_size_list': fish_size_list})

def fish_favorite_list(request):
    fish_favorite_list = FishInfo.objects.order_by('-good')
    return render(request, 'fish_favorite_list.html', {'fish_favorite_list': fish_favorite_list})

#詳細情報、いいねカウント
def fish_info(request, fish_info_id):
    fish_info = get_object_or_404(FishInfo, pk=fish_info_id)
    favorites_count = Favorite.objects.filter(fish=fish_info).count()  # お気に入りの数をカウント
    return render(request, 'fish_info.html', {'fish_info': fish_info, 'good_count': favorites_count})

# ジャンルIDに対応するFishInfo レコードを取得
def genre(request, genre):
    fish_infos_genre = FishInfo.objects.filter(genre=genre)
    return render(request, 'genre_list.html', {'fish_infos_genre': fish_infos_genre})

#いいね機能
from .models import Favorite
def favorite_toggle(request, fish_info_id):
    user = request.user
    fish = get_object_or_404(FishInfo, pk=fish_info_id)
    favorite, created = Favorite.objects.get_or_create(user=user, fish=fish)

    if not created:
        favorite.delete()# すでにいいねが存在する場合は、いいねを削除
    return redirect('fish_info', fish_info_id=fish_info_id)  # 適切なビュー名に置き換えてください

#お気に入り画面表示
def favorite_list(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user).select_related('fish')
    fish_info_favorite = [favorite.fish for favorite in favorites]
    return render(request, 'favorite_list.html', {'fish_info_favorite': fish_info_favorite})

#自分の魚
def my_fish(request):
    my_fish_list = FishInfo.objects.filter(user=request.user)
    return render(request, 'my_fish.html', {'my_fish_list': my_fish_list})
    

#検索機能
from django.db.models import Q
from django.urls import reverse
# フォームからのPOSTリクエストを処理するビュー
def search_fish_info(request):
    if request.method == 'POST':# POSTリクエストを受け取った場合
        query = request.POST.get('q', '')# フォームから検索クエリを取得
        return redirect(f"{reverse('search_results')}?q={query}")# 検索クエリをURLパラメータに含めて、検索結果表示ビューにリダイレクト
    return render(request, 'search_form.html')# 検索後も再度検索を表示する

# 検索結果を表示
def search_results(request):
    query = request.GET.get('q', '')# GETリクエストから検索クエリを取得
    if query:# 検索クエリに基づいてFishInfoオブジェクトを検索
        fish_info_search = FishInfo.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
    else:
        fish_info_search = FishInfo.objects.none()# 検索クエリが空の場合は、空のクエリセットを生成
    return render(request, 'search.html', {'fish_info_search': fish_info_search, 'query': query})

#アイコン選択機能
from .models import UserProfile, Icon
from django.contrib.auth.decorators import login_required

@login_required
def icon_change(request):
    if request.method == 'POST':
        icon_id = request.POST.get('icon_id')
        new_icon = Icon.objects.get(id=icon_id)
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.icon = new_icon
        user_profile.save()
        return redirect('setting')  # ユーザーの設定ページへリダイレクト
    else:
        icons = Icon.objects.all()
        return render(request, 'icon_change.html', {'icons': icons})

    
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

