from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # השם הנכון כאן

    def __str__(self):
        return f"Customer {self.id} - {self.user.username}"

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        (1, 'Meat'),
        (2, 'Milk'),
        (3, 'Ice Cream'),
        (4, 'Drink'),
        (5, 'Bread'),
    ]

    id = models.AutoField(primary_key=True)
    product_type = models.IntegerField(choices=PRODUCT_TYPE_CHOICES)  # השם הנכון כאן
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product {self.id} - {self.description}"

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # השם הנכון כאן
    products = models.ManyToManyField(Product)  # השם הנכון כאן
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for User {self.user.username}"

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # השם הנכון כאן
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # השם הנכון כאן
    amount = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # חישוב מחיר כולל
        self.total_price = self.product.price * self.amount
        super(OrderDetail, self).save(*args, **kwargs)

    def __str__(self):
        return f"OrderDetail {self.id} with Product {self.product.id} for Cart {self.cart.id}"
