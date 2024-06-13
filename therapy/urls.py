from . import views
from django.urls import path
app_name = 'therapy'

urlpatterns = [
    path('', views.index, name='index'),
]
