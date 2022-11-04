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
        

class SetTeamPlaceModelSerializer(serializers.Serializer):
    """Set Team  place serializer."""

    def update(self, instance, data):
        """Update team place."""
        group = instance
        team_first_place = group[0]
        team_second_place = group[1]
        team_third_place = group[2]
        team_fourth_place = group[3]
        team_first_place.first_place = True
        team_first_place.second_place = False
        team_first_place.save()
        team_second_place.first_place = False
        team_second_place.second_place = True
        team_second_place.save()
        team_third_place.first_place = False
        team_third_place.second_place = False
        team_third_place.save()
        team_fourth_place.first_place = False
        team_fourth_place.second_place = False
        team_fourth_place.save()
        
        return group