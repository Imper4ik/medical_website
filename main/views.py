from django.shortcuts import render

# Create your views here.


from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def specialties(request):
    return render(request, 'main/specialties.html')


def contact(request):
    return render(request, 'main/contact.html')


def appointment(request):
    return render(request, 'main/appointment.html')
