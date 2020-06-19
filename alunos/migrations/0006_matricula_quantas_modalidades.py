# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros_basicos', '0006_turma_dias_de_aula'),
        ('alunos', '0005_auto_20161226_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='quantas_modalidades',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastros_basicos.Promocao', verbose_name='Quantas modalidades o aluno vai fazer?'),
        ),
    ]