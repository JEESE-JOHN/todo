from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('features.tasks.urls')),
    path('api/music/', include('features.music.urls')),
    path('api/artists/', include('features.artists.urls')),
]