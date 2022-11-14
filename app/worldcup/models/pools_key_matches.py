"""Worldcup matches models."""
from datetime import date
from enum import unique
from django.db import models

# Models
from .teams import Team
from users.models.users import User
from .worldcup_pools import WorldcupPool

class PoolKeyMatch(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_1_key_pool', verbose_name='Team 1  ')
    team_1_goals = models.IntegerField(default=0, verbose_name='Team 1 goals')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_2_key_pool', verbose_name='Team 2 ')
    team_2_goals = models.IntegerField(default=0, verbose_name='Team 2 goals ')
    penalties = models.BooleanField(default=False, verbose_name='Penaltie')
    team_1_penalty_goals = models.IntegerField(default=0, verbose_name='penalties')
    team_2_penalty_goals = models.IntegerField(default=0, verbose_name='penalties')
    team_winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_winner_pool', verbose_name='winner', blank=True, null=True)
    team_loser = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_loser_pool', verbose_name='loser', blank=True, null=True)
    round = models.CharField(max_length=24, verbose_name='Round', null=True, blank=True)
    match_number = models.IntegerField(default=0, verbose_name='match number')
    match_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Key match date', blank=True, null=True)
    started = models.BooleanField(default=False, verbose_name='started')
    finished = models.BooleanField(default=False, verbose_name='finished')
    analized = models.BooleanField(default=False, verbose_name='Analized')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_key_pool', verbose_name='User')
    pool = models.ForeignKey(WorldcupPool, on_delete=models.CASCADE, related_name='worldcup_key_pool', verbose_name='pool')
    pool_match_points = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.team_1} vs {self.team_2}'
    
    class Meta:
        verbose_name_plural = "Pool key matches"
        ordering = ["match_number"]