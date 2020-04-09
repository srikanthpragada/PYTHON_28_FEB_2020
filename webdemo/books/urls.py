
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.book_home),
    path('list/', views.book_list),
    path('add/', views.book_add),
    path('delete/<int:id>', views.book_delete),
    path('edit/<int:id>', views.book_edit),
    path('search/', views.book_search),
    path('dosearch/', views.book_do_search),
]
