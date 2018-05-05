# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-04-30 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_categoria_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='status',
            field=models.CharField(blank=True, choices=[('C', 'Concluído'), ('CD', 'Cancelada')], default='', max_length=5, verbose_name='Status'),
        ),
    ]
