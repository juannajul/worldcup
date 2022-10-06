"""Oficial matches serializers."""

# Django rest framework
from tokenize import group
from rest_framework import serializers

# Models
from worldcup.models.worldcup_matches import WorldcupMatch
from worldcup.models.teams import Team

class WorldcupMatchModelSerializer(serializers.ModelSerializer):
    """Worldcup model serializer."""

    class Meta:
        model = WorldcupMatch
        fields = '__all__'
        

class CreateWorldcupMatchModelSerializer(serializers.ModelSerializer):
    """Create worldcup serializer."""
    team_1 = serializers.CharField(max_length=12)
    team_2 = serializers.CharField(max_length=12)
    match_number = serializers.IntegerField()
    match_date = serializers.DateTimeField()
    round = serializers.IntegerField()
    group = serializers.CharField(max_length=12)


    class Meta:
        model = WorldcupMatch
        fields = '__all__'

    def create(self, data):
        """Create match."""
        team_1_code = data['team_1']
        team_2_code = data['team_2']
        team_1 = Team.objects.get(team_code=team_1_code)
        team_2 = Team.objects.get(team_code=team_2_code)
        data['team_1'] = team_1
        data['team_2'] = team_2
        
        data = WorldcupMatch.objects.create(**data)

        return data