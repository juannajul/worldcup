"""Teams views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

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

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateTeamModelSerializer
        return TeamModelSerializer

    
    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly]
        return [p() for p in permissions]
    

