from rest_framework import serializers
from django.db.models import Avg


from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    
    class Meta:
        model = Post
        fields = '__all__'


    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg'] if instance.ratings.all().exists() else 0
        return rep