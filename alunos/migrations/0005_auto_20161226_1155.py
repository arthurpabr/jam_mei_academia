# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-26 11:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0004_auto_20161011_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='dia_de_vencimento',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(28)]),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='numero_celular',
            field=models.CharField(max_length=30, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='numero_fixo',
            field=models.CharField(max_length=30, verbose_name='Fixo'),
        ),
    ]
