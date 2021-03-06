# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-22 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_furnizimi_klienti_shitje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kodi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodi', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='furnizimi',
            options={'ordering': ('-data_porosise',), 'verbose_name': 'Furnizimi', 'verbose_name_plural': 'Furnizimet'},
        ),
        migrations.AlterModelOptions(
            name='inventari',
            options={'ordering': ('-kodiI',), 'verbose_name': 'Inventari', 'verbose_name_plural': 'Inventari'},
        ),
        migrations.AlterModelOptions(
            name='klienti',
            options={'ordering': ('-emer',), 'verbose_name': 'Klienti', 'verbose_name_plural': 'Klientet'},
        ),
        migrations.AlterModelOptions(
            name='shitje',
            options={'ordering': ('-data_porosise',), 'verbose_name': 'Shitje', 'verbose_name_plural': 'Shitjet'},
        ),
        migrations.RemoveField(
            model_name='inventari',
            name='kodi',
        ),
        migrations.AlterField(
            model_name='furnizimi',
            name='kodiF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kodiF', to='management.Kodi'),
        ),
        migrations.AlterField(
            model_name='furnizimi',
            name='permasat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='furnizimi',
            name='sasia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventari',
            name='gjendje',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventari',
            name='permasat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shitje',
            name='kodiS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kodiS', to='management.Kodi'),
        ),
        migrations.AlterField(
            model_name='shitje',
            name='sasia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventari',
            name='kodiI',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='kodiI', to='management.Kodi'),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='furnizimi',
            index_together=set([('kodiF', 'data_porosise')]),
        ),
        migrations.AlterIndexTogether(
            name='shitje',
            index_together=set([('kodiS', 'klienti')]),
        ),
    ]
