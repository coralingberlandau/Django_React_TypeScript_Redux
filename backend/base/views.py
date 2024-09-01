from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User 
from rest_framework import viewsets
from .models import Customer, Product, Cart, OrderDetail
from .serializers import CustomerSerializer, ProductSerializer, CartSerializer, OrderDetailSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# URL : http://127.0.0.1:8000/products/

# URL : http://127.0.0.1:8000/products/2/ - for update and delete

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# URL : http://127.0.0.1:8000/carts/

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# URL : http://127.0.0.1:8000/order-details/

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# register -- http://127.0.0.1:8000/register/
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response({'Success': 'new user born'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def priverty(req):
  return Response({'priverty': 'success'})

@api_view(['GET'])
def index(req):
   return Response({'hello': 'world'})


@api_view(['GET'])
def test(req):
   return Response({'test': 'success'})
