from django.shortcuts import render
from .models import Book
from django.views.generic import ListView

# Create your views here.
#my git file broke so all my commits got eaten up i had to reset and i lost my bitch daysie she died today tribute
class BookListView(ListView):
    model = Book
    template = 'book_list.html'
    context_object_name = "books"
