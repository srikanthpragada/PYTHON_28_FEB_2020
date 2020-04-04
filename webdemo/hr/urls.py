
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('index/', views.index),
    path('employees/', views.list_employees),
]
