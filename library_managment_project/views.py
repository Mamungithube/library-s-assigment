from django.shortcuts import render
from libraryapp.models import Book_category, Book


def home(request ,category_slug=None):
    book = Book.objects.all()
    
    if category_slug is not None:
        tmp = Book_category.objects.get(slug = category_slug)
        book = Book.objects.filter(category = tmp)
    category = Book_category.objects.all()
    return render(request,'index.html',{'book': book, 'categorys': category})



# def category_view(request, category_slug):
#     # Get the category based on the slug
#     category = get_object_or_404(Book_category, slug=category_slug)
    
#     # Get all books in the selected category
#     books = Book.objects.filter(category=category)
    
#     # Get all categories for the sidebar or dropdown
#     categories = Book_category.objects.all()
#     print(categories)
    
#     # Prepare the context data
#     context = {
#         'books': books,
#         'categories': categories,
#         'selected_category': category,
#         # 'is_homepage': False,
#         # 'total_result': books.count(),
#     }
    
#     # Render the template with the context data
#     return render(request, 'index.html', context)