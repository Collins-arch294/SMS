# Generated by Django 4.2.2 on 2023-06-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='type',
            field=models.CharField(choices=[('Reported Online', 'O'), ('Reported ERP', 'E')], max_length=50),
        ),
    ]
