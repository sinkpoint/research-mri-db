# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'conditions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Disorders',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('hemisphere', models.CharField(blank=True, max_length=255, choices=[('l', 'left'), ('r', 'right')])),
                ('operated', models.IntegerField(null=True, blank=True)),
                ('treatment_date', models.DateField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('condition', models.ForeignKey(blank=True, to='patientdb.Conditions', null=True)),
            ],
            options={
                'db_table': 'disorders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Educations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'educations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('parent_id', models.IntegerField(null=True, blank=True)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
            ],
            options={
                'db_table': 'groups',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mris',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('alias', models.CharField(max_length=255, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('freesurfer', models.BooleanField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('disorder', models.ForeignKey(blank=True, to='patientdb.Disorders', null=True)),
            ],
            options={
                'db_table': 'mris',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MriSchedules',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('patient_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('duration', models.FloatField()),
                ('confirmed', models.IntegerField()),
                ('done', models.IntegerField()),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'mri_schedules',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MriTypes',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'mri_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('handedness', models.CharField(max_length=1, choices=[('l', 'left'), ('r', 'right'), ('a', 'ambidextrous')])),
                ('firstname', models.CharField(max_length=255, db_column='firstName', blank=True)),
                ('lastname', models.CharField(max_length=255, db_column='lastName', blank=True)),
                ('middlename', models.CharField(max_length=255, db_column='middleName', blank=True)),
                ('gender', models.CharField(blank=True, max_length=255, choices=[('m', 'male'), ('f', 'female')])),
                ('age', models.CharField(max_length=255, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('alias', models.CharField(max_length=255, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('phone', models.CharField(max_length=100, blank=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('education', models.ForeignKey(blank=True, to='patientdb.Educations', null=True)),
            ],
            options={
                'db_table': 'patients',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PatientsProjects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('patient', models.ForeignKey(to='patientdb.Patients')),
            ],
            options={
                'db_table': 'patients_projects',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('title', models.CharField(max_length=255, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'projects',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProjectStatuses',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'project_statuses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'results',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='project_status',
            field=models.ForeignKey(to='patientdb.ProjectStatuses'),
        ),
        migrations.AddField(
            model_name='projects',
            name='subjects',
            field=models.ManyToManyField(to='patientdb.Patients', through='patientdb.PatientsProjects'),
        ),
        migrations.AddField(
            model_name='patientsprojects',
            name='project',
            field=models.ForeignKey(to='patientdb.Projects'),
        ),
        migrations.AddField(
            model_name='patients',
            name='projs',
            field=models.ManyToManyField(to='patientdb.Projects', through='patientdb.PatientsProjects'),
        ),
        migrations.AddField(
            model_name='mris',
            name='mri_type',
            field=models.ForeignKey(blank=True, to='patientdb.MriTypes', null=True),
        ),
        migrations.AddField(
            model_name='disorders',
            name='patient',
            field=models.ForeignKey(to='patientdb.Patients', to_field='patient_id'),
        ),
        migrations.AddField(
            model_name='disorders',
            name='result',
            field=models.ForeignKey(blank=True, to='patientdb.Results', null=True),
        ),
    ]
