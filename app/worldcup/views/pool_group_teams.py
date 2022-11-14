"""Pool group views."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializers
from worldcup.serializers.pool_group_teams import (PoolTeamModelSerializer, SetPlacesPointsPoolTeamGroupModelSerializer,
    AnalizePoolGroupMatchesModelSerializer
)
from worldcup.serializers.worldcup_pool import WorldcupPoolModelSerializer
# Models 
from worldcup.models.pool_group_teams import PoolTeam
from worldcup.models.pools_matches import PoolMatch
from worldcup.models.worldcup_pools import WorldcupPool

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PoolTeamViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Worldcup matches view set"""

    #queryset = WorldcupPool.objects.all()
    lookup_field = 'pool'

    def get_serializer_class(self):
        """Return serializer based on actions"""
        #if self.action == 'create':
        #    return CreateWorldcupPoolModelSerializer
        return PoolTeamModelSerializer

    
    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        return [p() for p in permissions]
    
    def get_queryset(self): 
        if self.action == 'teams_by_pool':
            return PoolTeam.objects.filter(pool=self.kwargs['pool'])
        if self.action == 'teams_by_pool_and_group':
            url = self.kwargs['pool']
            pool = url.split('_')[0]
            group = url.split('_')[1]
            return PoolTeam.objects.filter(pool=pool, group=group)
        if self.action == 'set_group_places_points':
            return WorldcupPool.objects.all()
        if self.action == 'analize_pool_group_matches':
            return PoolMatch.objects.filter(pool=self.kwargs['pool'])
        return PoolTeam.objects.all()


    @action(detail=True, methods=["get"])
    def teams_by_pool(self, request, *args, **kwargs):
        """List teams by pool."""
        teams = self.get_queryset()
        serializer = PoolTeamModelSerializer(teams, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["get"])
    def teams_by_pool_and_group(self, request, *args, **kwargs):
        """List teams by pool."""
        teams = self.get_queryset()
        serializer = PoolTeamModelSerializer(teams, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=False, methods=["patch"])
    def set_group_places_points(self, request, *args, **kwargs):
        """Set team place."""
        pools = self.get_queryset()
        serializer = SetPlacesPointsPoolTeamGroupModelSerializer(instance=pools, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["patch"])
    def analize_pool_group_matches(self, request, *args, **kwargs):
        """Analize pool group matches."""
        matches = self.get_queryset()
        serializer = AnalizePoolGroupMatchesModelSerializer(instance=matches, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = WorldcupPoolModelSerializer(serializer).data
        return Response(data, status=status.HTTP_200_OK)


