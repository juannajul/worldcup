"""Pools matches models."""
from datetime import date
from email.policy import default
from django.db import models

# Models
from .teams import Team
from users.models.users import User
from .worldcup_pools import WorldcupPool

class PoolMatch(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='team_1_pools', verbose_name='Team 1')
    team_1_goals = models.IntegerField(default=0, verbose_name='Team 1 goals')
    team_2 = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='team_2_pools', verbose_name='Team 2')
    team_2_goals = models.IntegerField(default=0, verbose_name='Team 2 goals')
    match_number = models.IntegerField(default=0, verbose_name='Match number')
    match_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Match date')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='User')
    pool = models.ForeignKey(WorldcupPool, on_delete=models.CASCADE, related_name='worldcup_pool', verbose_name='Pool')
    round = models.IntegerField(default=0, verbose_name='Round')
    group = models.CharField(max_length=12, blank=False, null=False, verbose_name='Group')
    started = models.BooleanField(default=False, verbose_name='started')
    finished = models.BooleanField(default=False, verbose_name='finished')
    pool_match_points = models.IntegerField(default=0)
    analized = models.BooleanField(default=False, verbose_name='Analized')
    def __str__(self):
        return f'{self.team_1} vs {self.team_2}'

    class Meta:
        verbose_name_plural = "Pools matches"
        ordering = ["pool", "match_number", "group"]