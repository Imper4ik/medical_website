from django.shortcuts import render

# Create your views here.


def index(request):
    content = {'title': 'neurology'}
    return render(request,'neurology/index.html', content)