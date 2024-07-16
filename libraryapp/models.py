from django.db import models
from django.contrib.auth.models import User

class Book_category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,blank=True,unique=True)


    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    Book_image = models.ImageField(upload_to="book/media/uploads/")
    Book_name = models.CharField(max_length=200)
    Borrow_price = models.IntegerField()
    Book_description = models.CharField(max_length=200)
    Quantity = models.IntegerField(default = 0)
    category = models.ForeignKey(Book_category,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Book_name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.car.car_name}"
    

class PaymentModel(models.Model):
    Book_name=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    purchese_date=models.DateTimeField(auto_now_add=True)
    net_quantity=models.IntegerField()
    total_price=models.IntegerField()