from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Comment, Rating

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = ['comment']
        

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='onwer.email')
    rating = serializers.IntegerField(min_value=1, max_value=5)
    
    class Meta:
        model = Rating
        fields = ['owner', 'rating']



class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'comment', 'created_at'] 