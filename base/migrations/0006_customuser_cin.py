# Generated by Django 5.0.6 on 2024-07-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_paiement_preuve_paiement_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cin',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]