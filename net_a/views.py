from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

"""
ビューずどっとぱいがないときに、GPTが教えてくれたやつ
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,world!")
"""