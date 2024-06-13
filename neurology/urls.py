from . import views
from django.urls import path
app_name = 'neurology'

urlpatterns = [
    path('', views.index, name='index'),
]
