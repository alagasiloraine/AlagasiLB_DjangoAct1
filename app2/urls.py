from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('galleries/', views.galleries, name='galleries'),
    path('profile/', views.profile, name='profile'),
]
