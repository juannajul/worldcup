"""teams models."""
from distutils.command.upload import upload
from django.db import models

class Team(models.Model):
    country = models.CharField(max_length=50, unique=True , blank=False, null=False, verbose_name='Country name')
    group = models.CharField(max_length=12, blank=False, null=False, verbose_name='Group')
    flag_image = models.ImageField(upload_to='media/flags', blank=False, null=False, verbose_name='Flag image')
    team_code = models.CharField(max_length=3, blank=False, null=False, verbose_name='Team code')
    points = models.IntegerField(default=0, verbose_name='Team points')
    matches_played = models.IntegerField(default=0, verbose_name='Matches played')
    wins = models.IntegerField(default=0, verbose_name='teams wins')
    draws = models.IntegerField(default=0, verbose_name='teams draws')
    losses = models.IntegerField(default=0, verbose_name='teams losses')
    goals_for = models.IntegerField(default=0, verbose_name='Goals for')
    goals_against = models.IntegerField(default=0, verbose_name='Goals against')
    goal_difference = models.IntegerField(default=0 , verbose_name='Goal difference')

    def __str__(self):
        return self.country
