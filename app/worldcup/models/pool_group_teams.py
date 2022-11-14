"""teams models."""
from distutils.command.upload import upload
from tokenize import group
from django.db import models
from worldcup.models.teams import Team
from users.models.users import User
from .worldcup_pools import WorldcupPool

class PoolTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='pool_team', verbose_name='Team')
    team_code = models.SlugField(max_length=12, unique=False, verbose_name="Team slug")
    group = models.CharField(max_length=12, blank=False, null=False, verbose_name='Group')
    pool_team_points = models.IntegerField(default=0, verbose_name='Team points')
    matches_played = models.IntegerField(default=0, verbose_name='Matches played')
    pool = models.ForeignKey(WorldcupPool, on_delete=models.CASCADE, related_name='pool_team', verbose_name='Pool')
    wins = models.IntegerField(default=0, verbose_name='team wins')
    draws = models.IntegerField(default=0, verbose_name='team draws')
    losses = models.IntegerField(default=0, verbose_name='team losses')
    pool_team_goals_for = models.IntegerField(default=0, verbose_name='Goals for')
    pool_team_goals_against = models.IntegerField(default=0, verbose_name='Goals against')
    pool_team_goals_difference = models.IntegerField(default=0 , verbose_name='Goal difference')
    first_place = models.BooleanField(default=False, verbose_name='First place')
    second_place = models.BooleanField(default=False, verbose_name='Second place')

    def __str__(self):
        return self.team.country

    class Meta:
        verbose_name_plural = "Pool Teams"
        ordering = ["group" ,"-pool_team_points", "-pool_team_goals_difference", "-pool_team_goals_for"]
