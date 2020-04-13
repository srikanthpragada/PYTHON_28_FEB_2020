from django.views.generic import ListView
from .models import Book


class ListBooks(ListView):
    model = Book
    context_object_name = 'books'


