from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

"""my_pageへのURL設定"""
def my_page(request):
    return render(request, 'my_page.html')


"""
ビューずどっとぱいがないときに、GPTが教えてくれたやつ
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,world!")
"""


