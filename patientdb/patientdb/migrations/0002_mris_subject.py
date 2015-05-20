# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mris',
            name='subject',
            field=models.ForeignKey(default=-1, to='patientdb.Patients'),
            preserve_default=False,
        ),
    ]
