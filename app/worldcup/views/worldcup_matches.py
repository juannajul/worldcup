"""Oficial matches views."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializers
from worldcup.serializers.worldcup_matches import WorldcupMatchModelSerializer, CreateWorldcupMatchModelSerializer, FinishMatchModelSerializer

# Models 
from worldcup.models.worldcup_matches import WorldcupMatch

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

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
        permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_queryset(self): 
        if self.action == 'finish_match':
            print(self.kwargs)
            return WorldcupMatch.objects.filter(match_number=self.kwargs['match_number'])
        return WorldcupMatch.objects.all()


    @action(detail=True, methods=["patch"])
    def finish_match(self, request, *args, **kwargs):
        """Set pool match points."""
        match = self.get_queryset()
        serializer = FinishMatchModelSerializer(
            instance=match,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

