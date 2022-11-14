"""Worldcup pools serializers."""

# Django rest framework
from rest_framework import serializers

# Models
from worldcup.models.worldcup_pools import WorldcupPool

# Serializers 
from users.serializers.users import UserModelSerializer
from worldcup.models.teams import Team
from worldcup.models.pool_group_teams import PoolTeam

class WorldcupPoolModelSerializer(serializers.ModelSerializer):
    """worldcup pool model serializer."""
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = WorldcupPool
        fields = '__all__'
        

class CreateWorldcupPoolModelSerializer(serializers.ModelSerializer):
    """Create worldcup pool serializer."""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
     
    class Meta:
        model = WorldcupPool
        fields = '__all__'

    def create(self, data):
        """Create pool."""
        data = WorldcupPool.objects.create(**data)
        # Create pool team for pool
        teams = Team.objects.all()
        for team in teams:
            pool_team_data = {}
            pool_team_data['team'] = team
            pool_team_data['pool'] = data
            pool_team_data['group'] = team.group
            pool_team_data['team_code'] = team.team_code
            PoolTeam.objects.create(**pool_team_data)
        return data
        

class SetPoolPointsModelSerializer(serializers.ModelSerializer):
    """Set pool points serializer."""
    pass