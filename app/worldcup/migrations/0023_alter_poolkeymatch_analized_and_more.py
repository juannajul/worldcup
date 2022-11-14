# Generated by Django 4.1.1 on 2022-11-11 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup', '0022_alter_poolteam_options_poolteam_team_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poolkeymatch',
            name='analized',
            field=models.BooleanField(default=False, verbose_name='Analized'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='finished'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='match_number',
            field=models.IntegerField(default=0, verbose_name='match number'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='penalties',
            field=models.BooleanField(default=False, verbose_name='Penaltie'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worldcup_key_pool', to='worldcup.worldcuppool', verbose_name='pool'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='started',
            field=models.BooleanField(default=False, verbose_name='started'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='team_1_penalty_goals',
            field=models.IntegerField(default=0, verbose_name='penalties'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='team_2_penalty_goals',
            field=models.IntegerField(default=0, verbose_name='penalties'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='team_loser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_loser_pool', to='worldcup.team', verbose_name='loser'),
        ),
        migrations.AlterField(
            model_name='poolkeymatch',
            name='team_winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_winner_pool', to='worldcup.team', verbose_name='winner'),
        ),
        migrations.AlterField(
            model_name='poolmatch',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='finished'),
        ),
        migrations.AlterField(
            model_name='poolmatch',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worldcup_pool', to='worldcup.worldcuppool', verbose_name='Pool'),
        ),
        migrations.AlterField(
            model_name='poolmatch',
            name='started',
            field=models.BooleanField(default=False, verbose_name='started'),
        ),
        migrations.AlterField(
            model_name='poolmatch',
            name='team_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='team_1_pools', to='worldcup.team', verbose_name='Team 1'),
        ),
        migrations.AlterField(
            model_name='poolmatch',
            name='team_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='team_2_pools', to='worldcup.team', verbose_name='Team 2'),
        ),
        migrations.AlterField(
            model_name='poolteam',
            name='team_code',
            field=models.SlugField(max_length=12, verbose_name='Team slug'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='analized',
            field=models.BooleanField(default=False, verbose_name='match Analized'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='match finished'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='match_date',
            field=models.DateTimeField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='match_number',
            field=models.IntegerField(default=0, unique=True, verbose_name='Match number'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='penalties',
            field=models.BooleanField(default=False, verbose_name='Penalties'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='started',
            field=models.BooleanField(default=False, verbose_name='match started'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='team_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1_key', to='worldcup.team', verbose_name='Team 1'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='team_1_penalty_goals',
            field=models.IntegerField(default=0, verbose_name='Team 1 penalty'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='team_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2_key', to='worldcup.team', verbose_name='Team 2'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='team_2_goals',
            field=models.IntegerField(default=0, verbose_name='Team 2 goals'),
        ),
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='team_2_penalty_goals',
            field=models.IntegerField(default=0, verbose_name='Team 2 penalty'),
        ),
    ]
