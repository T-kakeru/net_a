from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    my_name = 'kakeru takehana'
    favourite_fruits = ['apple', 'grape', 'lemon']
    my_info = {
        'name': 'kakeru takehana',
        'age': 26        
    }
    return render(request, 'index.html', context={
        'my_name': my_name,
        'favourite_fruits': favourite_fruits,
        'my_info': my_info
    })


    """他に送りたいデータをここで定義"""
    

"""
ビューずどっとぱいがないときに、GPTが教えてくれたやつ
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,world!")
"""