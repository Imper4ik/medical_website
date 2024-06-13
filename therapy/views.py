from django.shortcuts import render

# Create your views here.

def index(request):
    content = {'title': 'therapy'}
    return render(request, 'therapy/index.html', content)