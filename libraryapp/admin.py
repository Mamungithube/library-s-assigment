from django.contrib import admin
from .models import Book,Profile,Comment,PaymentModel,Book_category
# Register your models here.

admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(PaymentModel)

class BookCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','slug']

admin.site.register(Book_category, BookCategory)