# tutorial/tables.py
import django_tables2 as tables
from patientdb.models import *
from django_tables2.utils import A  # alias for Accessor
from django.utils.safestring import mark_safe

class PatientTable(tables.Table):
    id = tables.LinkColumn('pat_view', args=[A('pk')])
    name = tables.Column(order_by=('lastname', 'firstname'))
    age_added = tables.Column(order_by=('birthday'))
    #controls = tables.TemplateColumn(template_name = 'patientdb/table_controls.html', attrs={'th':{'class':'rowlink-skip'}})

    def render_gender(self, value):
        icon = 'fa-venus'
        if value=='male':
            icon = 'fa-mars'
        return mark_safe('<i class="fa '+icon+'"></i> '+value)

    class Meta:
        model = Patients
        order_by = ('-modified')
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        fields = ('id','alias','name','gender','age_added','notes','created','modified')
        #exclude = ('age','birthday','firstname','lastname','middlename','education','phone','email','education_id','handedness')
        #sequence = ('id','alias','name','gender','age_added','notes')

class ProjectTable(tables.Table):
    id = tables.LinkColumn('proj_view', args=[A('pk')])
    status = tables.Column('status', accessor='project_status.name')
    num_subjects = tables.Column('num_subjects', sortable=False)

    def render_subjects(self, value, table):
        return value.all()

    class Meta:
        model = Projects
        fields = ('id','title','num_subjects','status','notes','created','modified')

class MriTable(tables.Table):
    id = tables.LinkColumn('mri_view', args=[A('pk')])
    subject = tables.Column(accessor='subject.name')
    disorder = tables.Column(accessor='disorder.condition.name', verbose_name='condition')
    mri_type = tables.Column(accessor='mri_type.name')
    time_to_treatment = tables.Column('time_to_treatment', order_by='date')
    class Meta:
        model = Mris
        fields = ('id','mri_type','subject','disorder','date','time_to_treatment','note')

class DisorderTable(tables.Table):
    condition = tables.Column(accessor='condition.name')
    result = tables.Column(accessor='result.name')
    class Meta:
        model = Disorders
        fields = ('condition','hemisphere','operated','treatment_date','result','notes')
