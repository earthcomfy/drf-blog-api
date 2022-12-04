from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("users.urls", namespace="users")),
    path("post/", include("posts.urls", namespace="posts")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
