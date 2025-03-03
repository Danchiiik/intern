from django.contrib import admin

from apps.feedback.models import Comment, Rating

admin.site.register(Comment)
admin.site.register(Rating)