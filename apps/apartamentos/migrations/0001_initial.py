# Generated by Django 5.0.4 on 2024-06-04 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bloco', '0001_initial'),
        ('inquilino', '0001_initial'),
        ('proprietario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('bloco', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='bloco.bloco')),
                ('morador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inquilino.inquilinos')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proprietario.proprietario')),
            ],
        ),
    ]
