from . import views
from django.urls import path
app_name = 'cardiology'

urlpatterns = [
    path('', views.index, name='cardiology'),
    path('infarct/', views.infarct, name='infarct'),
    path('aritmic/', views.aritmic, name='aritmic'),
    path('heart_failure/', views.heart_failure, name='heart_failure'),
]