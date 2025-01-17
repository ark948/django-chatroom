from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.authtoken.models import Token




from accounts.models import CustomUser



class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password"]



class UserRegisterSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "password2"]
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            detail = {
                "detail": "Email already taken."
            }
            raise ValidationError(detail=detail)
        return email
    
    def validate(self, instance):
        if instance['password'] != instance['password2']:
            raise ValidationError({'message': "Both passwords must match."})
        if CustomUser.objects.filter(email=instance['email']).exists():
            raise ValidationError({'message': "Email already taken."})
        return instance
    
    def create(self, validated_data):
        passowrd = validated_data.pop('password')
        passowrd2 = validated_data.pop('password2')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(passowrd)
        user.save()
        Token.objects.create(user=user)
        return user