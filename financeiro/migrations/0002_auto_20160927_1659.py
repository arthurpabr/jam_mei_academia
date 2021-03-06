# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-27 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensalidade',
            options={'verbose_name': 'Mensalidade', 'verbose_name_plural': 'Mensalidades'},
        ),
        migrations.AddField(
            model_name='mensalidade',
            name='situacao',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pendente'), (2, 'Cancelada'), (3, 'Paga')], default=1),
        ),
        migrations.AddField(
            model_name='mensalidade',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Valor pago'),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='mes_referencia',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'), (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')]),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='valor_cobrado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Valor cobrado'),
        ),
    ]
