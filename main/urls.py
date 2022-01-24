
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('contacts', views.contacts, name='contacts'),
    # path('admin', views.admin, name='admin'),
]
