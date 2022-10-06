"""Worldcup pools views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Serializers
from worldcup.serializers.worldcup_pool import WorldcupPoolModelSerializer, CreateWorldcupPoolModelSerializer

# Models 
from worldcup.models.worldcup_pools import WorldcupPool

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class WorldcupPoolViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Worldcup matches view set"""

    queryset = WorldcupPool.objects.all()

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateWorldcupPoolModelSerializer
        return WorldcupPoolModelSerializer

    
    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        return [p() for p in permissions]
    

