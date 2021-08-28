from generator.views import mainapp
from django.urls import path
from .views import *

urlpatterns = [
    path('', mainapp, name='main'),
    path('error/', error_page, name='error'),
    path('success/', success_page, name='success'),
]
