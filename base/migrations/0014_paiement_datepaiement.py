# Generated by Django 5.0.6 on 2024-07-18 16:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_paiement_nom_paiement_numero_paiement_refapp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiement',
            name='datePaiement',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
