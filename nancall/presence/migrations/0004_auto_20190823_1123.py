# Generated by Django 2.2.4 on 2019-08-23 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presence', '0003_auto_20190823_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nangroupe',
            name='added_by',
        ),
        migrations.AddField(
            model_name='nangroupe',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
