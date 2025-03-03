from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, required=True, write_only=True)

    class Meta:
        model = User 
        fields = ['email', 'password', 'password2', 'username', 'telegram_chat_id']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError('Passwords do not match')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "username", "telegram_chat_id"]  # Only include safe fields
