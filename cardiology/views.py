from django.shortcuts import render

# Create your views here.


def index(request):
    content = {'title': 'Main_Cardiology_page'}
    return render(request, 'cardiology/index.html', content)


def infarct(request):
    content = {'title': 'Infarct'}
    return render(request, 'cardiology/infarct_miokarda.html', content)


def aritmic(request):
    content = {'title': 'Aritmic'}
    return render(request, 'cardiology/aritmic.html', content)


def heart_failure(request):
    content = {'title': 'Heart_failure'}
    return render(request, 'cardiology/serd_nedost.html', content)


def heart_success(request):
    content = {'title': 'Main Ills'}
    return render(request, 'cardiology/main_ills.html', content)