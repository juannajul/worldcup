# Generated by Django 4.1.1 on 2022-12-02 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup', '0024_worldcuppool_group_analized'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['group', '-points', '-goals_difference', '-goals_for', 'team_code'], 'verbose_name_plural': 'Teams'},
        ),
    ]
