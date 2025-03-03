from apps.feedback.serializers import CommentListSerializer, RatingSerializer
from apps.posts.models import Post
from .models import Comment, Rating
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView



class FeedbackMixin:

    def get_comments(self, request, pk=None):
        """
        Retrieve all comments for a specific post.
        """
        try:
            post = self.get_object()  
            comments = Comment.objects.filter(post=post)  
            serializer = CommentListSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Post.DoesNotExist:
            return Response('Пост не найден', status=status.HTTP_404_NOT_FOUND)


    def add_comment(self, request, pk=None):
        try:
            post = self.get_object()
            comment = request.data['comment']
            user = request.user
            comment_obj = Comment.objects.create(owner=user, post=post, comment=comment)
            comment_obj.save()
            return Response('Комментарий добавлен', status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(f'Error: {e}', status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete_comment(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response('Комментарий удален', status=status.HTTP_404_NOT_FOUND)
    

    def edit_comment(self, request, pk):
        try:
            comment = get_object_or_404(Comment, pk=pk)
            
            new_comment = request.data.get('comment')
            if not new_comment:
                return Response('Комментарий не может быть пустым', status=status.HTTP_400_BAD_REQUEST)
            
            comment.comment = new_comment
            comment.save()

            return Response('Комментарий обновлен', status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response('Комментарий не найден', status=status.HTTP_404_NOT_FOUND)
    

    def rating(self, request, pk=None, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
            rating_obj.rating = request.data['rating']
            rating_obj.save()
            msg = request.data['rating']
            return Response(f'Вы поставили {msg} баллов')
        except:
            return Response('Something went wrong')
        



class CommentApiView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentListSerializer(comments, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
