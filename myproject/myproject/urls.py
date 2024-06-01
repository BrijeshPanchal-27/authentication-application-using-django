from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Maps the root URL to the index view
    path('about/', views.about, name='about'),  # Maps /about/ URL to the about view
    path('contact/', views.contact, name='contact'),  # Maps /contact/ URL to the contact view
    # Additional URL patterns can be added here
]
