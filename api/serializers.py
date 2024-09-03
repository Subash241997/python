from rest_framework import serializers
from .models import SignupUser

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = SignupUser
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate_email(self, value):
        if SignupUser.objects.filter(email = value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value
    
    def validate(self, data):
        # Check if any field is empty
        for field in ['email', 'first_name', 'last_name', 'password']:
            if not data.get(field):
                raise serializers.ValidationError(f"{field} field cannot be empty.")
            
        email = data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")
            
        # Custom validation for password
        password = data.get('password')
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError("Password must contain at least one number.")
        if not any(char in '!@#$%^&*()_+[]{}|;:,.<>?/' for char in password):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return data
    
    def create(self, validated_data):
        user = SignupUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password']) # Hash the password
        user.save()
        return user

class Loginserializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        email  = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = SignupUser.objects.get(email = email)
            except SignupUser.DoesNotExist:
                raise serializers.ValidationError('Invalid email or password')
        
            if not user.check_password(password):
                raise serializers.ValidationError('Invalid email or password')
        else:
            raise serializers.ValidationError("Something went wrong please try again later")

        data['user'] = user
        return data
    