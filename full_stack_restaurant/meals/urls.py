from django.urls import path
from . import views

urlpatterns = [
    path('', views.meals,name='home'),
    path('contact-us', views.contacts, name= 'contact-us')
]