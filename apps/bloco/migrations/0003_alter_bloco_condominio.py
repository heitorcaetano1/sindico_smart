# Generated by Django 5.0.4 on 2024-06-25 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloco', '0002_alter_bloco_condominio'),
        ('condominios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloco',
            name='condominio',
            field=models.ManyToManyField(blank=True, null=True, to='condominios.condominios'),
        ),
    ]
