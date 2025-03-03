from django.urls import path, include   
from rest_framework.routers import DefaultRouter

from apps.feedback.views import CommentApiView
from apps.posts.views import PostViewset

router = DefaultRouter()

router.register('', PostViewset)


urlpatterns = [
    path('<int:pk>/mark_add/', PostViewset.as_view({'post': 'rating'})),
    path('<int:pk>/comment/', PostViewset.as_view({'post': 'add_comment'})),
    path('<int:pk>/comments/', PostViewset.as_view({'get': 'get_comments'})),
    path('comment/<int:pk>/', PostViewset.as_view({'delete': 'delete_comment'})),
    path('comm/<int:pk>/', PostViewset.as_view({'put': 'edit_comment'})),
    path('', include(router.urls))
]
