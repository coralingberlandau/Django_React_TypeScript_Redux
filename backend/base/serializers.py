from rest_framework import serializers
from .models import Customer, Product, Cart, OrderDetail

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'city', 'street', 'phone', 'image', 'user']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_type', 'price', 'description', 'image', 'created_time']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'created_time']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id', 'cart', 'product', 'amount', 'total_price', 'created_time']
