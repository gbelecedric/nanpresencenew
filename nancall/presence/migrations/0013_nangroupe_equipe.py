# Generated by Django 2.2.4 on 2019-09-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0012_jours_cours_weekday'),
    ]

    operations = [
        migrations.AddField(
            model_name='nangroupe',
            name='equipe',
            field=models.PositiveIntegerField(null=True),
        ),
    ]