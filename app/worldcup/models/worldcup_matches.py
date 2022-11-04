"""Worldcup matches models."""
from datetime import date
from django.db import models

# Models
from .teams import Team

class WorldcupMatch(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_1', verbose_name='Team 1')
    team_1_goals = models.IntegerField(default=0, verbose_name='Team 1 goals')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_2', verbose_name='Team 2')
    team_2_goals = models.IntegerField(default=0, verbose_name='Team 2 goals')
    match_number = models.IntegerField(default=0, verbose_name='Match number')
    match_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Match date')
    round = models.IntegerField(default=0, verbose_name='Round')
    group = models.CharField(max_length=12, blank=False, null=False, verbose_name='Group')
    started = models.BooleanField(default=False, verbose_name='Match started')
    finished = models.BooleanField(default=False, verbose_name='Match finished')
    analized = models.BooleanField(default=False, verbose_name='worldcup match Analized')

    def __str__(self):
        return f'{self.team_1} vs {self.team_2}'
    
    class Meta:
        verbose_name_plural = "Worldcup matches"
        ordering = ["match_number", "group"]