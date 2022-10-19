"""Worldcup pools views."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

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

    #queryset = WorldcupPool.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'username'

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateWorldcupPoolModelSerializer
        return WorldcupPoolModelSerializer

    
    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        return [p() for p in permissions]
    
    def get_queryset(self): 
        if self.action == 'pool_by_username':
            print(self.kwargs)
            return WorldcupPool.objects.filter(user__username=self.kwargs.get(self.lookup_url_kwarg))
        return WorldcupPool.objects.all()


    @action(detail=True, methods=["get"])
    def pool_by_username(self, request, *args, **kwargs):
        """List pool by username."""
        pools = self.get_queryset()
        serializer = WorldcupPoolModelSerializer(pools, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

