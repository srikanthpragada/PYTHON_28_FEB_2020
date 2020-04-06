
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('index/', views.index),
    path('employees/', views.list_employees),
    path('countries/', views.list_countries),
    path('add_employee/', views.add_employee),
]
