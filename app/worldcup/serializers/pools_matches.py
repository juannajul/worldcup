"""Pools matches serializers."""

# Django rest framework
from multiprocessing import context, pool
from rest_framework import serializers

# Models
from worldcup.models.pools_matches import PoolMatch
from worldcup.models.teams import Team
from worldcup.models.worldcup_pools import WorldcupPool
from worldcup.models.worldcup_matches import WorldcupMatch
from worldcup.models.pool_group_teams import PoolTeam

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
    

class FinishPoolMatchesModelSerializer(serializers.Serializer):
    """Finish match serializer."""

    def update(self, instance , data):
        """Finish match."""
        if len(instance) > 0:
            matches = instance 
            for match in matches:
                pool_team_1 = PoolTeam.objects.get(team_code=match.team_1.team_code, pool=match.pool)
                pool_team_2 = PoolTeam.objects.get(team_code=match.team_2.team_code, pool=match.pool)
                team_1_goals = match.team_1_goals
                team_2_goals = match.team_2_goals
                if team_1_goals > team_2_goals:
                    # Team 1 wins
                    #match.finished = True
                    #match.save()
                    # Pool teams
                    pool_team_1.pool_team_points += 3
                    pool_team_1.wins += 1
                    pool_team_2.losses += 1
                    pool_team_1.pool_team_goals_for += team_1_goals
                    pool_team_1.pool_team_goals_against += team_2_goals
                    pool_team_1.pool_team_goals_difference = pool_team_1.pool_team_goals_for - pool_team_1.pool_team_goals_against
                    pool_team_2.pool_team_goals_for += team_2_goals
                    pool_team_2.pool_team_goals_against += team_1_goals
                    pool_team_2.pool_team_goals_difference = pool_team_2.pool_team_goals_for - pool_team_2.pool_team_goals_against
                    pool_team_1.save()
                    pool_team_2.save()
                elif team_1_goals < team_2_goals:
                    # Team 2 wins
                    #match.finished = True
                    #match.save()
                    # Pool teams
                    pool_team_2.pool_team_points += 3
                    pool_team_2.wins += 1
                    pool_team_1.losses += 1
                    pool_team_2.pool_team_goals_for += team_2_goals
                    pool_team_2.pool_team_goals_against += team_1_goals
                    pool_team_2.pool_team_goals_difference = pool_team_2.pool_team_goals_for - pool_team_2.pool_team_goals_against
                    pool_team_1.pool_team_goals_for += team_1_goals
                    pool_team_1.pool_team_goals_against += team_2_goals
                    pool_team_1.pool_team_goals_difference = pool_team_1.pool_team_goals_for - pool_team_1.pool_team_goals_against
                    pool_team_1.save()
                    pool_team_2.save()
                elif team_1_goals == team_2_goals:
                    # Draw
                    #match.finished = True
                    #match.save()
                    # Pool teams
                    pool_team_1.pool_team_points += 1
                    pool_team_2.pool_team_points += 1
                    pool_team_1.draws += 1
                    pool_team_2.draws += 1
                    pool_team_1.pool_team_goals_for += team_1_goals
                    pool_team_1.pool_team_goals_against += team_2_goals
                    pool_team_1.pool_team_goals_difference = pool_team_1.pool_team_goals_for - pool_team_1.pool_team_goals_against
                    pool_team_2.pool_team_goals_for += team_2_goals
                    pool_team_2.pool_team_goals_against += team_1_goals
                    pool_team_2.pool_team_goals_difference = pool_team_2.pool_team_goals_for - pool_team_2.pool_team_goals_against
                    pool_team_1.save()
                    pool_team_2.save()
                
            return instance
        else:
            raise serializers.ValidationError('there is no match finished')
            return data