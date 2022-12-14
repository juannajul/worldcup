# Generated by Django 4.1.1 on 2022-10-05 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worldcup', '0004_worldcupmatch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worldcupmatch',
            options={'ordering': ['match_number', 'group'], 'verbose_name_plural': 'Worldcup matches'},
        ),
        migrations.AlterField(
            model_name='worldcupmatch',
            name='round',
            field=models.IntegerField(default=0, verbose_name='Round'),
        ),
        migrations.CreateModel(
            name='WorldcupPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0, verbose_name='Pool Points')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pool_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Worldcup pools',
                'ordering': ['-points'],
            },
        ),
        migrations.CreateModel(
            name='PoolsMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1_goals', models.IntegerField(default=0, verbose_name='Team 1 goals')),
                ('team_2_goals', models.IntegerField(default=0, verbose_name='Team 2 goals')),
                ('match_number', models.IntegerField(default=0, verbose_name='Match number')),
                ('match_date', models.DateTimeField(verbose_name='Match date')),
                ('round', models.IntegerField(default=0, verbose_name='Round')),
                ('group', models.CharField(max_length=12, verbose_name='Group')),
                ('started', models.BooleanField(default=False, verbose_name='Match started')),
                ('finished', models.BooleanField(default=False, verbose_name='Match finished')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worldcup_pool', to='worldcup.worldcuppool', verbose_name='worldcup pool')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1_pools', to='worldcup.team', verbose_name='Team 1 pools')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2_pools', to='worldcup.team', verbose_name='Team 2 pools')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Pools matches',
                'ordering': ['match_number', 'group'],
            },
        ),
    ]
