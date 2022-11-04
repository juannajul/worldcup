# Generated by Django 4.1.1 on 2022-10-28 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup', '0010_alter_team_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldcupKeyMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1_goals', models.IntegerField(default=0, verbose_name='Team 1 goals key')),
                ('team_2_goals', models.IntegerField(default=0, verbose_name='Team 2 goals key')),
                ('penalties', models.BooleanField(default=False, verbose_name='Penalties key')),
                ('team_1_penalty_goals', models.IntegerField(default=0, verbose_name='Team 1 penalty goals')),
                ('team_2_penalty_goals', models.IntegerField(default=0, verbose_name='Team 2 penalty goals')),
                ('round', models.CharField(blank=True, max_length=24, null=True, verbose_name='Round')),
                ('match_number', models.IntegerField(default=0, verbose_name='Match number key')),
                ('match_date', models.DateTimeField(verbose_name='Key match date')),
                ('started', models.BooleanField(default=False, verbose_name='Key match started')),
                ('finished', models.BooleanField(default=False, verbose_name='Key match finished')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1_key', to='worldcup.team', verbose_name='Team 1 key')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2_key', to='worldcup.team', verbose_name='Team 2 key')),
                ('team_winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_winner', to='worldcup.team', verbose_name='Team winner')),
            ],
            options={
                'verbose_name_plural': 'Worldcup key matches',
                'ordering': ['match_number'],
            },
        ),
    ]