"""Pools teams serializers."""

# Django rest framework
from rest_framework import serializers

# Models
from worldcup.models.pool_group_teams import PoolTeam
from worldcup.models.worldcup_pools import WorldcupPool
from worldcup.models.worldcup_matches import WorldcupMatch
from worldcup.models.pools_matches import PoolMatch


# Serializers 
from worldcup.models.teams import Team
from worldcup.models.pool_group_teams import PoolTeam
from worldcup.serializers.worldcup_pool import WorldcupPoolModelSerializer
from worldcup.serializers.teams import TeamModelSerializer

class PoolTeamModelSerializer(serializers.ModelSerializer):
    """Pool team model serializer."""
    pool = WorldcupPoolModelSerializer(read_only=True)
    team = TeamModelSerializer(read_only=True)
    class Meta:
        model = PoolTeam
        fields = '__all__'

class AnalizePoolGroupMatchesModelSerializer(serializers.Serializer):
    
    def update(self, instance, data):
        pool_matches =  list(instance)
        pool = pool_matches[0].pool
        for match in pool_matches:
            team_1 = PoolTeam.objects.get(pool=pool, team=match.team_1)
            team_2 = PoolTeam.objects.get(pool=pool, team=match.team_2)
            team_1_goals = match.team_1_goals
            team_2_goals = match.team_2_goals
            if team_1_goals > team_2_goals:
                    # Team 1 wins
                    team_1.pool_team_points += 3
                    team_1.wins += 1
                    team_2.losses += 1
                    team_1.pool_team_goals_for += team_1_goals
                    team_1.pool_team_goals_against += team_2_goals
                    team_1.pool_team_goals_difference = team_1.pool_team_goals_for - team_1.pool_team_goals_against
                    team_2.pool_team_goals_for += team_2_goals
                    team_2.pool_team_goals_against += team_1_goals
                    team_2.pool_team_goals_difference = team_2.pool_team_goals_for - team_2.pool_team_goals_against
            elif team_1_goals < team_2_goals:
                # Team 2 wins
                team_2.pool_team_points += 3
                team_2.wins += 1
                team_1.losses += 1
                team_2.pool_team_goals_for += team_2_goals
                team_2.pool_team_goals_against += team_1_goals
                team_2.pool_team_goals_difference = team_2.pool_team_goals_for - team_2.pool_team_goals_against
                team_1.pool_team_goals_for += team_1_goals
                team_1.pool_team_goals_against += team_2_goals
                team_1.pool_team_goals_difference = team_1.pool_team_goals_for - team_1.pool_team_goals_against
            elif team_1_goals == team_2_goals:
                # Draw
                team_1.pool_team_points += 1
                team_2.pool_team_points += 1
                team_1.draws += 1
                team_2.draws += 1
                team_1.pool_team_goals_for += team_1_goals
                team_1.pool_team_goals_against += team_2_goals
                team_1.pool_team_goals_difference = team_1.pool_team_goals_for - team_1.pool_team_goals_against
                team_2.pool_team_goals_for += team_2_goals
                team_2.pool_team_goals_against += team_1_goals
                team_2.pool_team_goals_difference = team_2.pool_team_goals_for - team_2.pool_team_goals_against
            team_1.save()
            team_2.save()
        pool = WorldcupPool.objects.get(pk=pool.pk)
        pool.group_analized = True
        pool.save()
        return pool



class SetPlacesPointsPoolTeamGroupModelSerializer(serializers.Serializer):
    """Set places pool team group serializer."""
    
    def update(self, instance , data):
        """Set places pool team group."""
        groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for group in groups:
            pools = instance
            worldcup_teams = Team.objects.filter(group=group)
            for pool in pools:
                pool_teams = PoolTeam.objects.filter(pool=pool, group=group)
                pool_teams = pool_teams.order_by("-pool_team_points", "-pool_team_goals_difference", "-pool_team_goals_for")
                team_first_place = pool_teams[0]
                team_second_place = pool_teams[1]
                team_third_place = pool_teams[2]
                team_fourth_place = pool_teams[3]
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
                
                # Set points
                pool_team_1 = pool_teams[0]
                pool_team_2 = pool_teams[1]
                worldcup_team_1 = worldcup_teams[0]
                worldcup_team_2 = worldcup_teams[1]
                pool_team1_points = 0
                pool_team2_points = 0
                if pool_team_1.team_code == worldcup_team_1.team_code:
                    pool_team1_points = 4
                    print("entra1")
                elif pool_team_1.team_code == worldcup_team_2.team_code:
                    pool_team1_points = 3
                    print("entra2")
                
                if pool_team_2.team_code == worldcup_team_1.team_code:
                    pool_team2_points = 3
                    print("entra3")
                elif pool_team_2.team_code == worldcup_team_2.team_code:
                    pool_team2_points = 4
                    print("entra4")
                group_points = pool_team1_points + pool_team2_points
                pool.group_points += group_points
                pool.save()
        return instance