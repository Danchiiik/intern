from django.urls import path, include   
from rest_framework.routers import DefaultRouter

from apps.feedback.views import CommentApiView
from apps.posts.views import PostViewset

router = DefaultRouter()

router.register('', PostViewset)


urlpatterns = [
    path('<int:pk>/rating/', PostViewset.as_view({'post': 'rating'})),
    path('<int:pk>/comment/', PostViewset.as_view({'post': 'add_comment'})),
    path('comment/<int:pk>/', PostViewset.as_view({'delete': 'delete_comment'})),
    path('comment/<int:pk>/', PostViewset.as_view({'put': 'edit_comment'})),
    path('comment/', CommentApiView.as_view()),
    path('', include(router.urls))
]
