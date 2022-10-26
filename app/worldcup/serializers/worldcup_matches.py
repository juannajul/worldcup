"""Oficial matches serializers."""

# Django rest framework
from tokenize import group
from rest_framework import serializers

# Models
from worldcup.models.worldcup_matches import WorldcupMatch
from worldcup.models.teams import Team
from worldcup.models.pools_matches import PoolMatch

# Serializers
from worldcup.serializers.teams import TeamModelSerializer

class WorldcupMatchModelSerializer(serializers.ModelSerializer):
    """Worldcup model serializer."""
    team_1 = TeamModelSerializer(read_only=True)
    team_2 = TeamModelSerializer(read_only=True)

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

class StartMatchModelSerializer(serializers.Serializer):
    """Start match serializer."""
    def update(self, instance , data):
        """Start match."""
        
        match = instance
        match.started = True
        match.save()
        return instance

class FinishMatchModelSerializer(serializers.Serializer):
    """Finish match serializer."""

    def update(self, instance , data):
        """Finish match."""
        print(len(instance))
        print(instance)
        if len(instance) > 0:
            match = instance[0] 
            match_number = match.match_number
            data['match'] = match
            team_1 = Team.objects.get(team_code=instance[0].team_1.team_code)
            team_1_goals = match.team_1_goals
            team_2 = Team.objects.get(team_code=instance[0].team_2.team_code)
            team_2_goals = match.team_2_goals
            if team_1_goals > team_2_goals:
                # Team 1 wins
                team_1.points += 3
                team_1.wins += 1
                team_2.losses += 1
                team_1.goals_for += team_1_goals
                team_1.goals_against += team_2_goals
                team_1.goals_difference = team_1.goals_for - team_1.goals_against
                team_2.goals_for += team_2_goals
                team_2.goals_against += team_1_goals
                team_2.goals_difference = team_2.goals_for - team_2.goals_against
                match.finished = True
                team_1.save()
                team_2.save()
                match.save()
            elif team_1_goals < team_2_goals:
                # Team 2 wins
                team_2.points += 3
                team_2.wins += 1
                team_1.losses += 1
                team_2.goals_for += team_2_goals
                team_2.goals_against += team_1_goals
                team_2.goals_difference = team_2.goals_for - team_2.goals_against
                team_1.goals_for += team_1_goals
                team_1.goals_against += team_2_goals
                team_1.goals_difference = team_1.goals_for - team_1.goals_against
                match.finished = True
                team_1.save()
                team_2.save()
                match.save()
            elif team_1_goals == team_2_goals:
                # Draw
                team_1.points += 1
                team_2.points += 1
                team_1.draws += 1
                team_2.draws += 1
                team_1.goals_for += team_1_goals
                team_1.goals_against += team_2_goals
                team_1.goals_difference = team_1.goals_for - team_1.goals_against
                team_2.goals_for += team_2_goals
                team_2.goals_against += team_1_goals
                team_2.goals_difference = team_2.goals_for - team_2.goals_against
                match.finished = True
                team_1.save()
                team_2.save()
                match.save()
            
            pool_matches = PoolMatch.objects.filter(match_number=match_number)
            for pool_match in pool_matches:
                pool_match.finished = True
                pool_match.save() 

            
            return instance
        else:
            raise serializers.ValidationError('there is no match finished')
        return data