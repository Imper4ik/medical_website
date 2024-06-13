from django.shortcuts import render

# Create your views here.


def index(request):
    content = {'title': 'orthopedics'}
    return render(request, 'orthopedics/index.html', content)