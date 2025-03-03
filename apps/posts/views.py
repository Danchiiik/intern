from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.viewsets import  ModelViewSet

from apps.feedback.views import FeedbackMixin
from apps.posts.models import Post
from apps.posts.permissions import  IsStaff
from apps.posts.serializers import PostSerializer
from apps.posts.utils import send_telegram_message

from rest_framework.permissions import AllowAny

User = get_user_model()

class PostViewset(ModelViewSet, FeedbackMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get_permissions(self):
        if self.action == 'delete_comment' or self.action == 'edit_comment':
            return [IsStaff()]
        if self.action == 'add_comment':
            return [AllowAny()]
        return super().get_permissions()
        
    def perform_create(self, serializer):
        post = serializer.save(owner=self.request.user)
        
        if post.owner.telegram_chat_id:
            message = f"📝 {post.owner.username}, your post has been successfully created!"
            send_telegram_message(post.owner.telegram_chat_id, message)
