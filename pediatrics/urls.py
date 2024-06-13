from . import views
from django.urls import path
app_name = 'pediatrics'

urlpatterns = [
    path('', views.index, name='index'),
]
