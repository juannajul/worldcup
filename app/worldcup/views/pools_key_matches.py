"""Pool matches views."""

# Django rest framework
from multiprocessing import pool
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter


# Serializers
from worldcup.serializers.pools_key_matches import (
    PoolKeyMatchModelSerializer, CreatePoolKeyMatchModelSerializer, 
    SetPoolKeyMatchPointsModelSerializer, CreateQuarterFinalMatchModelSerializer,
    SavePoolKeyMatchResultModelSerializer, CreateSemiFinalMatchModelSerializer,
    CreateFinalMatchModelSerializer, Create3rdPlaceMatchModelSerializer, setpoolKeyMatchWinner)

# Models 
from worldcup.models.pools_key_matches import PoolKeyMatch
from worldcup.models.worldcup_pools import WorldcupPool
# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class PoolKeyMatchViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Pool matches view set"""

    queryset = PoolKeyMatch.objects.all()
    lookup_field = 'match_number'
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('match_number', 'pool')

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreatePoolKeyMatchModelSerializer
        if self.action == 'create_pool_quarter_finals':
            return CreateQuarterFinalMatchModelSerializer
        if self.action == 'create_pool_semifinal_finals':
            return CreateSemiFinalMatchModelSerializer
        if self.action == 'create_pool_finals':
            return CreateFinalMatchModelSerializer
        if self.action == 'create_pool_3rdPlace':
            return Create3rdPlaceMatchModelSerializer
        if self.action == 'save_pool_key_match_results':
            return SavePoolKeyMatchResultModelSerializer
        return PoolKeyMatchModelSerializer

    
    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        return [p() for p in permissions]

    def get_queryset(self): 
        if self.action == 'pool_key_matches_by_pool':
            return PoolKeyMatch.objects.filter(pool=self.kwargs['match_number'])
        if self.action == 'set_pool_key_match_points':
            return PoolKeyMatch.objects.filter(finished=True,analized=False)
        if self.action == 'get_matches_by_round':
            round = self.kwargs['match_number']
            return PoolKeyMatch.objects.filter(round=round)
        if self.action == 'get_matches_by_round_and_pool':
            url = self.kwargs['match_number']
            round = url.split('_')[0]
            pool = url.split('_')[1]
            return PoolKeyMatch.objects.filter(round=round, pool=pool)
        if self.action == 'save_pool_key_match_results':
            url = self.kwargs['match_number']
            url_list = url.split('_')
            match_number = int(url_list[0])
            pool = WorldcupPool.objects.get(pk=url_list[1])
            return PoolKeyMatch.objects.filter(pool=pool, match_number=match_number)
        if self.action == 'set_pool_key_match_winner':
            PoolKeyMatch.objects.all()
        return PoolKeyMatch.objects.all()

    
    @action(detail=False, methods=["post"])
    def create_pool_quarter_finals(self, request, *args, **kwargs):
        """Create pool quarter finals key."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = PoolKeyMatchModelSerializer(serializer.instance).data
        return Response(serializer, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["post"])
    def create_pool_semifinal_finals(self, request, *args, **kwargs):
        """Create pool quarter finals key."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = PoolKeyMatchModelSerializer(serializer.instance).data
        return Response(serializer, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=["post"])
    def create_pool_3rdPlace(self, request, *args, **kwargs):
        """Create pool quarter finals key."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = PoolKeyMatchModelSerializer(serializer.instance).data
        return Response(serializer, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=["post"])
    def create_pool_finals(self, request, *args, **kwargs):
        """Create pool quarter finals key."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = PoolKeyMatchModelSerializer(serializer.instance).data
        return Response(serializer, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=["patch"])
    def save_pool_key_match_results(self, request, *args, **kwargs):
        """Save pool key match results."""
        pool_key_match = self.get_queryset()
        serializer = self.get_serializer(
            instance=pool_key_match, 
            data=request.data, 
            partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_matches_by_round(self, request, *args, **kwargs):
        matches = self.get_queryset()
        serializer = PoolKeyMatchModelSerializer(matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_matches_by_round_and_pool(self, request, *args, **kwargs):
        matches = self.get_queryset()
        serializer = PoolKeyMatchModelSerializer(matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def pool_key_matches_by_pool(self, request, *args, **kwargs):
        """List pool matches by pool."""
        pool_matches = self.get_queryset()
        serializer = PoolKeyMatchModelSerializer(pool_matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=False, methods=["patch"])
    def set_pool_key_match_points(self, request, *args, **kwargs):
        #Set pool match points.
        pool_matches = self.get_queryset()
        print(pool_matches)
        serializer = SetPoolKeyMatchPointsModelSerializer(
            instance=pool_matches,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = PoolKeyMatchModelSerializer(pool_matches, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["patch"])
    def set_pool_key_match_winner(self, request, *args, **kwargs):
        #Set pool match points.
        pool_matches = self.get_queryset()
        print(pool_matches)
        serializer = setpoolKeyMatchWinner(
            instance=pool_matches,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = PoolKeyMatchModelSerializer(pool_matches, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    
    