from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Article

def article_list(request):
    list = Article.objects.all()
    search = request.GET.get('q','')
    if search:
        qs = Article.objects.filter(title__icontains=search)
    # <input type="text" name="q" value="{{q}}" /> 이렇게 설계되어 잇음. 
    return render(request,'article/article_list.html',{'article_list':search})

def detail(request, id):
    target = Article.objects.get(id=id)
    return render(request,'article/article_detail.html',{'article':target})

article_list2 = None

article_new = None

article_edit = None

article_delete = None
