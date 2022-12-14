"""Worldcup pools models."""
from datetime import date
from django.db import models

# Models
from users.models.users import User

class WorldcupPool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pool_user', verbose_name='User')
    points = models.IntegerField(default=0, verbose_name='Pool Points')
    round_group_points = models.IntegerField(default=0, verbose_name='Group Points')
    round_key_points = models.IntegerField(default=0, verbose_name='Key Points')
    group_points = models.IntegerField(default=0, verbose_name='Group Points')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    group_analized = models.BooleanField(default=False, verbose_name='Group Analized')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Worldcup pools"
        ordering = ["-points"]