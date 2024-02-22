from django.shortcuts import render

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


"""
オブジェクト化したい
for page in pages:
    def index(request):
        return render(request, str(page) + '.html')
        

"""

"""
ビューずどっとぱいがないときに、GPTが教えてくれたやつ
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,world!")
"""


