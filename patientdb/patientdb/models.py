# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Conditions(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'conditions'


class Disorders(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patient = models.ForeignKey('Patients')
    condition = models.ForeignKey('Conditions',blank=True, null=True)
    hemisphere = models.CharField(max_length=255, blank=True,choices=(('l','left'),('r','right')))
    operated = models.BooleanField(default=False)
    treatment_date = models.DateField(blank=True, null=True)
    result = models.ForeignKey('Results',blank=True, null=True)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'disorders'


class Educations(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'educations'


class Groups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    parent_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'groups'


class MriSchedules(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patient_id = models.IntegerField()
    project_id = models.IntegerField()
    event_date = models.DateTimeField()
    duration = models.FloatField()
    confirmed = models.IntegerField()
    done = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        managed = True
        db_table = 'mri_schedules'


class MriTypes(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'mri_types'


class Mris(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mri_type = models.ForeignKey('MriTypes',blank=True, null=True)
    subject = models.ForeignKey('Patients')
    disorder = models.ForeignKey('Disorders',blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    freesurfer = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    @property
    def time_to_treatment(self):
        if self.disorder.operated and self.disorder.treatment_date:
            return self.date - self.disorder.treatment_date
        return ''

    class Meta:
        managed = True
        db_table = 'mris'

class Patients(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    handedness = models.CharField(max_length=1, choices=[('l','left'),('r','right'),('a','ambidextrous')])
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=255, blank=True)  # Field name made lowercase.
    gender = models.CharField(max_length=255, blank=True, choices=[('m','male'),('f','female')])
    age = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    alias = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True, auto_now=True)
    education = models.ForeignKey('Educations',blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

    projs = models.ManyToManyField('Projects', through='PatientsProjects')

    @property
    def age_added(self):
        if self.created and self.birthday:
            dt = self.created.year - self.birthday.year
            return dt
        return -1

    @property
    def age_to_date(self):
        from datetime import date
        return self.birthday.year - date.today().year


    @property
    def name(self):
        return self.firstname + ' ' + self.middlename + ' ' + self.lastname

    class Meta:
        managed = True
        db_table = 'patients'



class ProjectStatuses(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'project_statuses'


class Projects(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True)
    project_status = models.ForeignKey('ProjectStatuses')

    subjects = models.ManyToManyField(Patients, through='PatientsProjects')

    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    notes = models.TextField(blank=True)

    @property
    def num_subjects(self):
        return len(self.subjects.all())

    class Meta:
        managed = True
        db_table = 'projects'


class PatientsProjects(models.Model):
    patient = models.ForeignKey('Patients')
    project = models.ForeignKey('Projects')
    #created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = True
        db_table = 'patients_projects'


class Results(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = True
        db_table = 'results'
