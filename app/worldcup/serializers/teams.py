"""Teams serializers."""

# Django rest framework
from rest_framework import serializers

# Models
from worldcup.models.teams import Team

class TeamModelSerializer(serializers.ModelSerializer):
    """Team model serializer."""

    class Meta:
        model = Team
        fields = '__all__'
        

class CreateTeamModelSerializer(serializers.ModelSerializer):
    """Create team serializer."""
    class Meta:
        model = Team
        fields = (
            'country', 
            'group',
            'flag_image',
            'team_code',
            )
        

class SetTeamPlaceModelSerializer(serializers.ModelSerializer):
    """Team model serializer."""
    team = TeamModelSerializer(read_only=True)
    first_place = serializers.BooleanField(required=True)
    second_place = serializers.BooleanField(required=True)

    class Meta:
        model = Team
        fields = ('first_place', 'second_place', 'team')