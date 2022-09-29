"""Users Urls"""

# Django rest framework
from rest_framework.routers import DefaultRouter

#Django
from django.urls import path, include

# Views
from .views import users as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]