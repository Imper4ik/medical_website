from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'cardiology/index.html')


def infarct(request):
    return render(request, 'cardiology/infarct_miokarda.html')


def aritmic(request):
    return render(request, 'cardiology/aritmic.html')


def heart_failure(request):
    return render(request, 'cardiology/serd_nedost.html')