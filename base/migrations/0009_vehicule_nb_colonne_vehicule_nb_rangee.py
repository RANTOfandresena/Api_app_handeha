# Generated by Django 5.0.6 on 2024-07-08 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_customuser_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='nb_colonne',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicule',
            name='nb_rangee',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
