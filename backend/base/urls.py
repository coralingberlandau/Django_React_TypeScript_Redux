########### application ############

from django.contrib import admin
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, CartViewSet, OrderDetailViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'order-details', OrderDetailViewSet)

urlpatterns = [
   path('', views.index),
   path('test/', views.test),
   path('priverty/', views.priverty),
   path('login/', views.MyTokenObtainPairView.as_view()),
   path('register/', views.register),
   path('', include(router.urls)),
]