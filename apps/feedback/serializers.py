from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Comment, Rating

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='onwer.email')
    rating = serializers.IntegerField(min_value=1, max_value=5)
    
    class Meta:
        model = Rating
        fields = ['owner', 'rating']



class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['owner', 'comment', 'created_at'] 