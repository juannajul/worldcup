"""Oficial matches views."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializers
from worldcup.serializers.worldcup_matches import WorldcupMatchModelSerializer, CreateWorldcupMatchModelSerializer, FinishMatchModelSerializer, StartMatchModelSerializer

# Models 
from worldcup.models.worldcup_matches import WorldcupMatch

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser

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
    
    def get_permissions(self):
        permissions = []
        if self.action in ['create', 'update', 'partial_update', 'finish_match', 'start_match']:
            permissions.append(IsAuthenticatedOrReadOnly)
            permissions.append(IsAdminUser)
        if self.action == 'get_started_matches':
            permissions.append(IsAuthenticatedOrReadOnly)
        return [p() for p in permissions]

    def get_queryset(self): 
        if self.action == 'finish_match':
            print(self.kwargs)
            return WorldcupMatch.objects.filter(match_number=self.kwargs['match_number'], started=True)
        if self.action == 'start_match':
            print(self.kwargs)
            return WorldcupMatch.objects.get(match_number=self.kwargs['match_number'])
        if self.action == 'get_started_matches':
            return WorldcupMatch.objects.filter(started=True, finished=False)
        if self.action == 'get_played_matches':
            return WorldcupMatch.objects.filter(started=True, finished=True)
        if self.action == 'get_analized_matches':
            return WorldcupMatch.objects.filter(analized=True)
        return WorldcupMatch.objects.all()


    @action(detail=True, methods=["patch"])
    def start_match(self, request, *args, **kwargs):
        """Start match."""
        match = self.get_queryset()
        serializer = StartMatchModelSerializer(instance=match, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        match = serializer.save()
        data = WorldcupMatchModelSerializer(match).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def get_started_matches(self, request, *args, **kwargs):
        """Get started matches."""
        matches = self.get_queryset()
        serializer = WorldcupMatchModelSerializer(matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def get_played_matches(self, request, *args, **kwargs):
        """Get started matches."""
        matches = self.get_queryset()
        serializer = WorldcupMatchModelSerializer(matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"])
    def get_analized_matches(self, request, *args, **kwargs):
        """Get started matches."""
        matches = self.get_queryset()
        serializer = WorldcupMatchModelSerializer(matches, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=True, methods=["patch"])
    def finish_match(self, request, *args, **kwargs):
        """Finish match and set teams points."""
        match = self.get_queryset()
        serializer = FinishMatchModelSerializer(
            instance=match,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

