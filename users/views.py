from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserRegistrationSerializer, UserProdcutSerializer, UserLoginSerializer, ProductSerializer
from .models import UserProfile, Product
from users.models import userProducts

#for creating Restframework User registration view
class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            }
        
        return Response(response, status=status_code)


#for creating restframework user login view
class UserLoginView(RetrieveAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = ProductSerializer(Product.objects.all())
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            # 'data':
            # [{
            #         'Products' : product.data
            #         }]
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)