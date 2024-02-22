from django.shortcuts import render

def index(request):
    return render(request, 'sign_up.html')
def index(request):
    return render(request, 'sign_in.html')
def index(request):
    return render(request, 'setting.html')
def index(request):
    return render(request, 'search.html')
def index(request):
    return render(request, 'privacy.html')
def index(request):
    return render(request, 'net_a_tutorial.html')
def my_page(request):
    return render(request, 'my_page.html')
def index(request):
    return render(request, 'my_fish.html')
def index(request):
    return render(request, 'history.html')
def index(request):
    return render(request, 'fish_info.html')
def index(request):
    return render(request, 'favorite.html')
def index(request):
    return render(request, 'edit_fish_check.html')
def index(request):
    return render(request, 'base.html')
def index(request):
    return render(request, 'add_fish_check.html')
def index(request):
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


