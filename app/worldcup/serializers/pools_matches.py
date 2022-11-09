"""Pools matches serializers."""

# Django rest framework
from multiprocessing import context
from rest_framework import serializers

# Models
from worldcup.models.pools_matches import PoolMatch
from worldcup.models.teams import Team
from worldcup.models.worldcup_pools import WorldcupPool
from worldcup.models.worldcup_matches import WorldcupMatch

# Serializers
from worldcup.serializers.teams import TeamModelSerializer

class PoolMatchModelSerializer(serializers.ModelSerializer):
    """Pool match model serializer."""
    team_1 = TeamModelSerializer(read_only=True)
    team_2 = TeamModelSerializer(read_only=True)

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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


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

class SetPoolMatchPointsModelSerializer(serializers.Serializer):
    """Set pool match points serializer."""
    
    def update(self, instance , data):
        """Set pool match points."""
        print(self.data)
        if len(instance) <= 0:
            raise serializers.ValidationError('There are not matches to set points.')
        else:
            for pool_match in instance:
                pool = WorldcupPool.objects.get(id=pool_match.pool.id)
                match_number = pool_match.match_number
                pool_match_points = 0
                worldcup_match = WorldcupMatch.objects.get(match_number=match_number)
                pool_team_1_goals = pool_match.team_1_goals
                pool_team_2_goals = pool_match.team_2_goals
                worldcup_team_1_goals = worldcup_match.team_1_goals
                worldcup_team_2_goals = worldcup_match.team_2_goals
                
                if pool_team_1_goals > pool_team_2_goals and worldcup_team_1_goals > worldcup_team_2_goals:
                    # Team 1 wins
                    pool_match_points = 3
                    
                    if pool_team_1_goals == worldcup_team_1_goals and pool_team_2_goals == worldcup_team_2_goals:
                        # Exact result
                        pool_match_points = 5
                elif pool_team_1_goals < pool_team_2_goals and worldcup_team_1_goals < worldcup_team_2_goals:
                    # Team 2 wins
                    pool_match_points = 3
                    
                    if pool_team_1_goals == worldcup_team_1_goals and pool_team_2_goals == worldcup_team_2_goals:
                        # Exact result
                        pool_match_points = 5
                elif pool_team_1_goals == pool_team_2_goals and worldcup_team_1_goals == worldcup_team_2_goals:
                    # Draw
                    pool_match_points = 3
                    
                    if pool_team_1_goals == worldcup_team_1_goals and pool_team_2_goals == worldcup_team_2_goals:
                        # Exact result
                        pool_match_points = 5

                # Pool
                print(pool_match_points)
                pool.points += pool_match_points
                pool.round_group_points += pool_match_points
                pool.save()

                # Pool match
                pool_match.pool_match_points = pool_match_points
                pool_match.analized = True
                pool_match.save()

                # Worldcup match
                worldcup_match.analized = True
                worldcup_match.save()

        return instance
    