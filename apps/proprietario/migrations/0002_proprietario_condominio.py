# Generated by Django 5.0.4 on 2024-06-11 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominios', '0001_initial'),
        ('proprietario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proprietario',
            name='condominio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='condominios.condominios'),
        ),
    ]
