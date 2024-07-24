from django.shortcuts import render
from libraryapp.models import Book_category, Book


def home(request ,category_slug=None):
    book = Book.objects.all()
    
    if category_slug is not None:
        tmp = Book_category.objects.get(slug = category_slug)
        book = Book.objects.filter(category = tmp)
    category = Book_category.objects.all()
    return render(request,'index.html',{'book': book, 'categorys': category})
