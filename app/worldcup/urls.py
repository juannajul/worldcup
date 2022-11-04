"""Teams Urls"""

# Django rest framework
from rest_framework.routers import DefaultRouter

#Django
from django.urls import path, include

# Views
from .views import teams as teams_views
from .views import worldcup_matches as worldcup_matches_views
from .views import worldcup_pools as worldcup_pools_views
from .views import pool_matches as pool_matches_views
from .views import worldcup_key_matches as worldcup_key_matches_views

router = DefaultRouter()
router.register(r'teams', teams_views.TeamViewSet, basename='teams')
router.register(r'worldcup_matches', worldcup_matches_views.WorldcupMatchViewSet, basename='worldcup_matches')
router.register(r'worldcup_pools', worldcup_pools_views.WorldcupPoolViewSet, basename='worldcup_pools')
router.register(r'pool_matches', pool_matches_views.PoolMatchViewSet, basename='pool_matches')
router.register(r'worldcup_key_matches', worldcup_key_matches_views.WorldcupKeyMatchViewSet, basename='worldcup_key_matches')

urlpatterns = [
    path('', include(router.urls))
]