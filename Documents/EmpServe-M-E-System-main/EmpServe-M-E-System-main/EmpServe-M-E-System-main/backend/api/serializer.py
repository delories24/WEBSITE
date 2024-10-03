
from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import User
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'confirm_password'] 

    def validate(self, attrs):
        # Check if passwords match
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        # Remove confirm_password from validated_data
        validated_data.pop('confirm_password')

        # Check for duplicate email
        if User.objects.filter(email=validated_data['email']).exists():
            raise ValidationError({'email': 'This email is already registered.'})

        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


 

'''class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','fullname', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user'''




 



    
