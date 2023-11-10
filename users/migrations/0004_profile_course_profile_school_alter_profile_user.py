# Generated by Django 4.2.2 on 2023-06-21 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]