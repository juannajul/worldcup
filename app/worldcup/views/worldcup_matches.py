"""Oficial matches views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Serializers
from worldcup.serializers.worldcup_matches import WorldcupMatchModelSerializer, CreateWorldcupMatchModelSerializer

# Models 
from worldcup.models.worldcup_matches import WorldcupMatch

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class WorldcupMatchViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Teams view set"""

    queryset = WorldcupMatch.objects.all()
    lookup_field = 'match_number'

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateWorldcupMatchModelSerializer
        return WorldcupMatchModelSerializer

    """
    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        return [p() for p in permissions]
    """

