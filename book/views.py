from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Book
from .forms import BookForm

book_new = CreateView.as_view(model=Book, fields='__all__')
book_list = ListView.as_view(model=Book)


def book_edit(request, id):
    pass
 