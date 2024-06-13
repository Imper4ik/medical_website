from django.shortcuts import render

# Create your views here.


def index(request):
    content = {'title': 'surgery'}
    return render(request, 'surgery/index.html', content)

