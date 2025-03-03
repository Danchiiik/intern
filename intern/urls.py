from django.contrib import admin
from django.urls import path, include


from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(openapi.Info(
    title = 'Choose Me API',
    default_version= '0.1',
    description= 'Hello my friend, it is swagger',
),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('apps.users.urls')),
    path('api/posts/', include('apps.posts.urls')),
    path('swagger/', schema_view.with_ui('swagger')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

