from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark


bookmark_list = ListView.as_view(model=Bookmark)
bookmark_detail = DetailView.as_view(model=Bookmark)
    