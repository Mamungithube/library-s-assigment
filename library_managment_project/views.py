from django.shortcuts import render
from libraryapp.models import Book_category, Book

def home(request, brand_slug = None):
    car_data = Book.objects.all()
    if brand_slug is not None:
        tmp = Book_category.objects.get(slug=brand_slug)
        car_data = Book.objects.filter(Brand_name = tmp)
    brands = Book_category.objects.all()
    return render(request,'index.html',{'data': car_data,'brand': brands})