# Generated by Django 5.0.2 on 2024-02-16 15:43

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('education_process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Login')),
                ('password', models.CharField(blank=True, verbose_name='Password')),
                ('last_name', models.CharField(blank=True, max_length=130, verbose_name='Last name')),
                ('first_name', models.CharField(blank=True, max_length=130, verbose_name='First name')),
                ('middle_name', models.CharField(blank=True, max_length=130, verbose_name='Middle name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, verbose_name='Gender')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth_date')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('user_status', models.CharField(choices=[('teacher', 'Teacher'), ('pupil', 'Pupil')], max_length=15, verbose_name='User status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pupils', to='education_process.grade', verbose_name='Studying a ___th grade')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pupils', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pupil',
                'verbose_name_plural': 'Pupils',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('group_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to='education_process.grade', verbose_name='Class teacher')),
                ('subjects', models.ManyToManyField(blank=True, related_name='teachers', to='education_process.subject', verbose_name='Teach subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
