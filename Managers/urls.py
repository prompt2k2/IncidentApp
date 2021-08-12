from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManagerVForm, name='ManagerVForm'),
    path('mlist/', views.ManagerList, name='ManagerList')
]