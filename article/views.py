from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Article

def article_list(request):
    print(request.user)
    qs = Article.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = Article.objects.filter(title__icontains=q)
    # <input type="text" name="q" value="{{q}}" /> 이렇게 설계되어 잇음. 
    return render(request,'article/article_list.html',{'article_list':qs,'q':q})

def detail(request, id):
    target = Article.objects.get(id=id)
    return render(request,'article/article_detail.html',{'article':target})

article_list2 = None

article_new = None

article_edit = None

article_delete = None
