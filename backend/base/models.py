from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # שדה user במקום userId

    fields = ['id', 'city', 'street', 'phone', 'user']

    def __str__(self):
        return f"Customer {self.id} - {self.user.username}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productType = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    createdTime = models.DateTimeField(auto_now_add=True)

    fields = ['id', 'productType', 'price', 'description', 'createdTime']

    def __str__(self):
        return f"Product {self.id} - {self.description}"


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # חיבור בין עגלה למשתמש
    products = models.ManyToManyField(Product)  # שימוש בשדה ManyToManyField לחיבור למוצרים
    createdTime = models.DateTimeField(auto_now_add=True)

    fields = ['id', 'user', 'products', 'createdTime']

    def __str__(self):
        return f"Cart {self.id} for User {self.user.username}"


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # שימוש ב-totalPrice
    createdTime = models.DateTimeField(auto_now_add=True)

    fields = ['id', 'cart', 'product', 'amount', 'createdTime', 'totalPrice']  # שימוש ב-totalPrice

    def save(self, *args, **kwargs):
        # חישוב מחיר כולל
        self.totalPrice = self.product.price * self.amount  # שימוש ב-totalPrice
        super(OrderDetail, self).save(*args, **kwargs)

    def __str__(self):
        return f"OrderDetail {self.id} with Product {self.product.id} for Cart {self.cart.id}"
