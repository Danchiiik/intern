from django.db import models

from apps.users.models import CustomUser


class Post(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"Post {self.id}"
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'