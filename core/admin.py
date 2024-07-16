from django.contrib import admin
from .models import Transaction,UserAccount
# Register your models here.
admin.site.register(Transaction)
admin.site.register(UserAccount)