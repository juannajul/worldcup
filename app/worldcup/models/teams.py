"""teams models."""
from distutils.command.upload import upload
from django.db import models

class Team(models.Model):
    country = models.CharField(max_length=50, unique=True , blank=False, null=False, verbose_name='Country name')
    group = models.CharField(max_length=12, blank=False, null=False, verbose_name='Group')
    team_code = models.SlugField(max_length=12, unique=True, verbose_name="Team slug")
    flag_image = models.ImageField(upload_to='media/flags', blank=False, null=False, verbose_name='Flag image')
    points = models.IntegerField(default=0, verbose_name='Team points')
    matches_played = models.IntegerField(default=0, verbose_name='Matches played')
    wins = models.IntegerField(default=0, verbose_name='team wins')
    draws = models.IntegerField(default=0, verbose_name='team draws')
    losses = models.IntegerField(default=0, verbose_name='team losses')
    goals_for = models.IntegerField(default=0, verbose_name='Goals for')
    goals_against = models.IntegerField(default=0, verbose_name='Goals against')
    goal_difference = models.IntegerField(default=0 , verbose_name='Goal difference')
    first_place = models.BooleanField(default=False, verbose_name='First place')
    second_place = models.BooleanField(default=False, verbose_name='Second place')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = "Teams"
        ordering = ["-points", "-goal_difference", "-goals_for"]
