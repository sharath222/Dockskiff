from rest_framework import serializers
from .models import UserProfile
from .models import User, userProducts, Product
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

# serializng userproduct data
class UserProdcutSerializer(serializers.ModelSerializer):
    model = userProducts
    fields = ('user','product')

# serializing user data
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number')

# serializing product data
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name','product_type', 'product_price')

# serializing registration data
class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            phone_number=profile_data['phone_number'],
        )
        return user

# serializing login data
class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    #validating request coming from user
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )

        return {
            'email':user.email,
        }