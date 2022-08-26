from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Book
from .forms import BookForm, BookModelForm

# book_new = CreateView.as_view(model=Book, fields='__all__')
book_list = ListView.as_view(model=Book)


# def book_new(request):
#     if request.method=='POST':
#         form = BookForm(request.POST,request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             book = Book.objects.create(**form.cleaned_data)
#             return redirect(book)
#     else:
#         form = BookForm()
#     return render(request,"book/book_form2.html",{'form':form})

def book_new(request):
    if request.method=='POST':
        form = BookModelForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # book = Book.objects.create(**form.cleaned_data)
            book = form.save(commit=False)
            book.ip = request.META['REMOTE_ADDR']
           
            book.save()
            return redirect(book)
    else:
        form = BookModelForm()
    return render(request,"book/book_form2.html",{'form':form})

def book_edit(request, id):
    book = get_object_or_404(Book,id=id)
    if request.method =='POST':
        form = BookModelForm(request.POST,request.FILES, instance=book)
        if form.is_valid():
            print(form.cleaned_data)
            # book = Book.objects.create(**form.cleaned_data)
            book = form.save(commit=False)
            book.ip = request.META['REMOTE_ADDR']
           
            book.save()
            return redirect(book)
    else:
        form = BookModelForm(instance=book)
    return render(request,"book/book_form2.html",{'form':form})
 