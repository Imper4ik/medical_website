from django.shortcuts import render

# Create your views here.


from django.shortcuts import render


def home(request):
    content = {'title': 'Home Page'}
    return render(request, 'main/home.html', content)


def specialties(request):
    content = {'title': 'Specialties Page'}
    return render(request, 'main/specialties.html',content)


def contact(request):
    content = {'title': 'Contact Page'}
    return render(request, 'main/contact.html', content)


def appointment(request):
    content = {'title': 'Appointment Page'}
    return render(request, 'main/appointment.html', content)
