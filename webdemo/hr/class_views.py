from django.views.generic import TemplateView, ListView
from .models import Book


class AboutView(TemplateView):
    template_name = 'about.html'


class ListBooks(ListView):
    model = Book

