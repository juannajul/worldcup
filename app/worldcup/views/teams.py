"""Teams views."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializers
from worldcup.serializers.teams import TeamModelSerializer, CreateTeamModelSerializer

# Models 
from worldcup.models.teams import Team

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TeamViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Teams view set"""

    queryset = Team.objects.all()
    lookup_field = 'team_code'
    lookup_url_kwarg = 'group'

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateTeamModelSerializer
        return TeamModelSerializer

    
    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        return [p() for p in permissions]

    def get_queryset(self): 
        if self.action == 'team_by_group':
            print(self.kwargs)
            return Team.objects.filter(group=self.kwargs['group'])
        return Team.objects.all()
    
    @action(detail=True, methods=["get"])
    def team_by_group(self, request, *args, **kwargs):
        """List team by group."""
        teams = self.get_queryset()
        serializer = TeamModelSerializer(teams, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

