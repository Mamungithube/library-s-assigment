from django.contrib import admin
from .models import Book,Profile,Comment,PaymentModel,Book_category
# Register your models here.

admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(PaymentModel)
admin.site.register(Book_category)