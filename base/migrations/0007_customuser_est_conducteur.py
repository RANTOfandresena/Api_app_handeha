# Generated by Django 5.0.6 on 2024-07-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_customuser_cin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='est_conducteur',
            field=models.BooleanField(default=False),
        ),
    ]
