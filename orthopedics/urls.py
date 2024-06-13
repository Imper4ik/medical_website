from . import views
from django.urls import path
app_name = 'orthopedics'

urlpatterns = [
    path('', views.index, name='index'),
]
