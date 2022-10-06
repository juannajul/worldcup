"""Pools matches serializers."""

# Django rest framework
from rest_framework import serializers

# Models
from worldcup.models.pools_matches import PoolMatch
from worldcup.models.teams import Team

class PoolMatchModelSerializer(serializers.ModelSerializer):
    """Pool match model serializer."""

    class Meta:
        model = PoolMatch
        fields = '__all__'
        

class CreatePoolMatchModelSerializer(serializers.ModelSerializer):
    """Create pool match serializer."""
    team_1 = serializers.CharField(max_length=12)
    team_1_goals = serializers.IntegerField()
    team_2 = serializers.CharField(max_length=12)
    team_2_goals = serializers.IntegerField()
    match_number = serializers.IntegerField()
    match_date = serializers.DateTimeField()
    round = serializers.IntegerField()
    group = serializers.CharField(max_length=12)


    class Meta:
        model = PoolMatch
        fields = '__all__'

    def create(self, data):
        """Create match."""
        team_1_code = data['team_1']
        team_2_code = data['team_2']
        team_1 = Team.objects.get(team_code=team_1_code)
        team_2 = Team.objects.get(team_code=team_2_code)
        data['team_1'] = team_1
        data['team_2'] = team_2
        
        data = PoolMatch.objects.create(**data)

        return data
