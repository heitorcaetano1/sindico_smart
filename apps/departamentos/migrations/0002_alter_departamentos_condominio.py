# Generated by Django 5.0.4 on 2024-06-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominios', '0001_initial'),
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentos',
            name='condominio',
            field=models.ManyToManyField(null=True, to='condominios.condominios'),
        ),
    ]
