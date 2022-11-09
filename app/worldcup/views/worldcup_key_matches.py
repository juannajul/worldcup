"""Oficial key matches views."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

# Serializers
from worldcup.serializers.worldcup_key_matches import (WorldcupKeyMatchModelSerializer, CreateWorldcupKeyMatchModelSerializer, 
    StartKeyMatchModelSerializer, CreateRoundOf16KeyMatchModelSerializer,
    FinishKeyMatchModelSerializer, CreateQuarterFinalsKeyMatchModelSerializer,
    CreateSemifinalKeyMatchModelSerializer, CreateFinalKeyMatchModelSerializer)

# Models 
from worldcup.models.worldcup_key_matches import WorldcupKeyMatch
from worldcup.models.teams import Team

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser

class WorldcupKeyMatchViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Key matches view set"""

    queryset = WorldcupKeyMatch.objects.all()
    lookup_field = 'match_number'
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('round',)

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateWorldcupKeyMatchModelSerializer
        if self.action == 'create_key_matches_roundOf16':
            return CreateRoundOf16KeyMatchModelSerializer
        if self.action == 'create_key_matches_roundOf8':
            return CreateQuarterFinalsKeyMatchModelSerializer
        if self.action == 'create_key_matches_semifinal':
            return CreateSemifinalKeyMatchModelSerializer
        if self.action == 'create_key_matches_final':
            return CreateFinalKeyMatchModelSerializer
        return WorldcupKeyMatchModelSerializer
    
    def get_permissions(self):
        permissions = []
        if self.action in ['create', 'update', 'partial_update', 'start_match',
            'create_key_matches_roundOf16','finish_match_roundOf16', 
            'create_key_matches_roundOf8', 'create_key_matches_semifinal',
            'create_key_matches_final']:
            permissions.append(IsAuthenticatedOrReadOnly)
            permissions.append(IsAdminUser)
        if self.action == 'get_started_matches':
            permissions.append(IsAuthenticatedOrReadOnly)
        return [p() for p in permissions]

    def get_queryset(self): 
        if self.action == 'finish_key_match':
            print(self.kwargs)
            return WorldcupKeyMatch.objects.filter(match_number=self.kwargs['match_number'], started=True)
        if self.action == 'start_match':
            print(self.kwargs)
            return WorldcupKeyMatch.objects.get(match_number=self.kwargs['match_number'])
        if self.action == 'get_started_matches':
            return WorldcupKeyMatch.objects.filter(started=True, finished=False)
        if self.action == 'get_played_matches':
            return WorldcupKeyMatch.objects.filter(started=True, finished=True)
        if self.action == 'get_matches_by_round':
            print(self.kwargs)
            return WorldcupKeyMatch.objects.filter(round=self.kwargs['match_number'])
        return WorldcupKeyMatch.objects.all()

    @action(detail=True, methods=['get'])
    def get_matches_by_round(self, request, *args, **kwargs):
        matches = self.get_queryset()
        serializer = WorldcupKeyMatchModelSerializer(matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def create_key_matches_roundOf16(self, request, *args, **kwargs):
        """Create key matches"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["post"])
    def create_key_matches_quarter_finals(self, request, *args, **kwargs):
        """Create key matches"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=["post"])
    def create_key_matches_semifinal(self, request, *args, **kwargs):
        """Create key matches"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["post"])
    def create_key_matches_final(self, request, *args, **kwargs):
        """Create key matches"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=["patch"])
    def start_match(self, request, *args, **kwargs):
        """Start match."""
        match = self.get_queryset()
        serializer = StartKeyMatchModelSerializer(instance=match, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        match = serializer.save()
        data = WorldcupKeyMatchModelSerializer(match).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def get_started_matches(self, request, *args, **kwargs):
        """Get started matches."""
        matches = self.get_queryset()
        serializer = WorldcupKeyMatchModelSerializer(matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def get_played_matches(self, request, *args, **kwargs):
        """Get started matches."""
        matches = self.get_queryset()
        serializer = WorldcupKeyMatchModelSerializer(matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["patch"])
    def finish_key_match(self, request, *args, **kwargs):
        #Set pool match points
        match = self.get_queryset()
        serializer = FinishKeyMatchModelSerializer(
            instance=match,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

