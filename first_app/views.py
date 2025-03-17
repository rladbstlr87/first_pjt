import random

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    my_name = 'yoonsick'

    context = {
        'my_name': my_name,
    }
    return render(request, 'hello.html', context)

def lunch(request):
    menu = ['설렁탕', '국밥', '김치찜']

    pick = random.choice(menu)

    context = {
        'pick': pick,
    }
    return render(request, 'lunch.html', context)

def lotto(request):

    numbers = random.sample(range(1, 46), 6)
    
    context = {
        'lotto': numbers
    }

    return render(request, 'lotto.html', context)