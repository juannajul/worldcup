"""Main Url's module"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/worldcup/', include(('worldcup.urls', 'worldcup'), namespace="worldcup")),
    path('api/auth/', include(('users.urls', 'users'), namespace="users")),
] 

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
