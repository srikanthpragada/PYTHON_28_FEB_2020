
from django.urls import path
from . import views, books_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('index/', views.index),
    path('employees/', views.list_employees),
    path('countries/', views.list_countries),
    path('add_employee/', views.add_employee),
    path('add_employee2/', views.add_employee_with_form),

    path('books/home/', books_views.book_home),
    path('books/list/', books_views.book_list),
    path('books/add/', books_views.book_add),
    path('books/delete/<int:id>', books_views.book_delete),
    path('books/edit/<int:id>', books_views.book_edit),
    path('books/search/', books_views.book_search),
    path('books/dosearch/', books_views.book_do_search),
]
