from rest_framework import serializers
from .models import Customer, Product, Cart, OrderDetail

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'city', 'street', 'phone', 'image', 'user']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productType', 'price', 'description', 'image', 'createdTime']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'createdTime']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id', 'cart', 'product', 'amount', 'totalPrice', 'createdTime']
