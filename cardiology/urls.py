from . import views
from django.urls import path
app_name = 'cardiology'

urlpatterns = [
    path('', views.index, name='cardiology'),
]