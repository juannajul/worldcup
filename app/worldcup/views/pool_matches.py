"""Pool matches views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Serializers
from worldcup.serializers.pools_matches import PoolMatchModelSerializer, CreatePoolMatchModelSerializer

# Models 
from worldcup.models.pools_matches import PoolMatch

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PoolMatchViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Pool matches view set"""

    queryset = PoolMatch.objects.all()

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreatePoolMatchModelSerializer
        return PoolMatchModelSerializer

    
    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        return [p() for p in permissions]
    

