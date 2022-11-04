"""Pool matches views."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


# Serializers
from worldcup.serializers.pools_matches import PoolMatchModelSerializer, CreatePoolMatchModelSerializer, SetPoolMatchPointsModelSerializer

# Models 
from worldcup.models.pools_matches import PoolMatch

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

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

    def get_queryset(self): 
        if self.action == 'pool_matches_by_pool':
            print(self.kwargs)
            return PoolMatch.objects.filter(pool=self.kwargs['pk'])
        if self.action == 'set_pool_match_points':
            return PoolMatch.objects.filter(finished=True,analized=False)
        return PoolMatch.objects.all()

    
    @action(detail=True, methods=["get"])
    def pool_matches_by_pool(self, request, *args, **kwargs):
        """List pool matches by pool."""
        pool_matches = self.get_queryset()
        serializer = PoolMatchModelSerializer(pool_matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=["patch"])
    def set_pool_match_points(self, request, *args, **kwargs):
        """Set pool match points."""
        pool_matches = self.get_queryset()
        print(pool_matches)
        serializer = SetPoolMatchPointsModelSerializer(
            instance=pool_matches,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = PoolMatchModelSerializer(pool_matches, many=True).data
        return Response(data, status=status.HTTP_200_OK)
