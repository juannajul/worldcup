# Generated by Django 4.1.1 on 2022-11-02 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup', '0013_worldcupkeymatch_analized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldcupkeymatch',
            name='match_number',
            field=models.IntegerField(default=0, unique=True, verbose_name='Match number key'),
        ),
    ]
