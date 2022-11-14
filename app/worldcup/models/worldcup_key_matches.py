"""Worldcup matches models."""
from datetime import date
from enum import unique
from django.db import models

# Models
from .teams import Team

class WorldcupKeyMatch(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_1_key', verbose_name='Team 1')
    team_1_goals = models.IntegerField(default=0, verbose_name='Team 1 goals key')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_2_key', verbose_name='Team 2')
    team_2_goals = models.IntegerField(default=0, verbose_name='Team 2 goals')
    penalties = models.BooleanField(default=False, verbose_name='Penalties')
    team_1_penalty_goals = models.IntegerField(default=0, verbose_name='Team 1 penalty')
    team_2_penalty_goals = models.IntegerField(default=0, verbose_name='Team 2 penalty')
    team_winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_winner', verbose_name='Team winner', blank=True, null=True)
    team_loser = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_loser', verbose_name='Team loser', blank=True, null=True)
    round = models.CharField(max_length=24, verbose_name='Round', null=True, blank=True)
    match_number = models.IntegerField(default=0, verbose_name='Match number', unique=True)
    match_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='date')
    started = models.BooleanField(default=False, verbose_name='match started')
    finished = models.BooleanField(default=False, verbose_name='match finished')
    analized = models.BooleanField(default=False, verbose_name='match Analized')

    def __str__(self):
        return f'{self.team_1} vs {self.team_2}'
    
    class Meta:
        verbose_name_plural = "Worldcup key matches"
        ordering = ["match_number"]