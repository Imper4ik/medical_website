from django.shortcuts import render

# Create your views here.


def index(request):
    content = {'title': 'pediatrics'}
    return render(request, 'pediatrics/index.html', content)