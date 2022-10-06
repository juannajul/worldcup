"""Worldcup pools models."""
from datetime import date
from django.db import models

# Models
from users.models.users import User

class WorldcupPool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pool_user', verbose_name='User')
    points = models.IntegerField(default=0, verbose_name='Pool Points')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Worldcup pools"
        ordering = ["-points"]