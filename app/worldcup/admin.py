from django.contrib import admin
from worldcup.models.teams import Team
from worldcup.models.worldcup_matches import WorldcupMatch
from worldcup.models.worldcup_pools import WorldcupPool
from worldcup.models.pools_matches import PoolMatch
from worldcup.models.worldcup_key_matches import WorldcupKeyMatch
from worldcup.models.pools_key_matches import PoolKeyMatch
from worldcup.models.pool_group_teams import PoolTeam

@admin.register(WorldcupPool)
class WorldcupPoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'points')
    list_display_links = ('id', 'user')

@admin.register(WorldcupMatch)
class WorldcupMatchAdmin(admin.ModelAdmin):
    list_display = ('match_number', 'team_1', 'team_1_goals', 'team_2', 'team_2_goals', 'group', 'round', 'started', 'finished', 'analized')
    list_display_links = ('match_number', 'team_1', 'team_2')
    list_filter = ('started', 'finished', 'analized')

@admin.register(WorldcupKeyMatch)
class WorldcupKeyMatchAdmin(admin.ModelAdmin):
    list_display = ('match_number', 'team_1', 'team_1_goals','team_1_penalty_goals','team_2', 'team_2_goals', 'team_2_penalty_goals', 'round', 'started', 'finished', 'analized')
    list_display_links = ('match_number', 'team_1', 'team_2')
    list_filter = ('started', 'finished', 'analized')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'country', 'group', 'points', 
        'wins', 'draws', 'losses', 'goals_for', 'goals_against', 
        'goals_difference', 'matches_played', 'first_place', 'second_place')
    list_display_links = ('id', 'country')
    list_filter = ('group', 'first_place', 'second_place')

@admin.register(PoolMatch)
class PoolMatchAdmin(admin.ModelAdmin):
    list_display = ('match_number', 'user','pool','team_1', 'team_1_goals', 'team_2', 'team_2_goals', 'pool_match_points', 'group', 'round', 'started', 'finished', 'analized')
    list_display_links = ('match_number', 'user', 'team_1', 'team_2')
    list_filter = ('started', 'finished', 'analized', 'pool')

@admin.register(PoolKeyMatch)
class PoolKeyMatchAdmin(admin.ModelAdmin):
    list_display = ('match_number', 'user', 'pool', 'pool_match_points',
    'team_1', 'team_1_goals','team_1_penalty_goals','team_2', 'team_2_goals', 
    'team_2_penalty_goals', 'round', 'started', 'finished', 'analized')
    list_display_links = ('match_number', 'user','team_1', 'team_2')
    list_filter = ('started', 'finished', 'analized' , 'pool')

@admin.register(PoolTeam)
class PoolTeamAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'team', 'pool', 'group', 'pool_team_points', 
        'wins', 'draws', 'losses', 'pool_team_goals_for', 'pool_team_goals_against', 
        'pool_team_goals_difference', 'matches_played', 'first_place', 'second_place')
    list_display_links = ('id', 'team')
    list_filter = ('group', 'first_place', 'second_place' , 'pool')

