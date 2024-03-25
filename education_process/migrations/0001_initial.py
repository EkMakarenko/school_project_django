# Generated by Django 5.0.2 on 2024-02-19 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=20, verbose_name='___ th grade')),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'List of grades',
            },
        ),
        migrations.CreateModel(
            name='RatingItemStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Mark status')),
            ],
            options={
                'verbose_name': 'Score status',
                'verbose_name_plural': 'List of scores status',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'List of school subjects',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.SmallIntegerField(choices=[(10, '10'), (9, '9'), (8, '8'), (7, '7'), (6, '6'), (5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], verbose_name='Mark')),
                ('created', models.DateField(blank=True, null=True, verbose_name='Date of creation')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education_process.grade', verbose_name='Class name')),
            ],
            options={
                'verbose_name': 'Gradebook',
                'verbose_name_plural': 'Marks',
            },
        ),
    ]
