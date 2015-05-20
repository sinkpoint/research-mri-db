from django.shortcuts import render
from django.db.models import Count
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django_tables2   import RequestConfig
from patientdb.models import *
from patientdb.tables import *

@login_required
def index(request):
    return render(request, 'patientdb/index.html')

@login_required
def login(request):
    return render(request, 'patientdb/login.html')

@login_required
def mri_index(request):
    pass_data = {}
    qset = Mris.objects.all()
    tab = MriTable(qset)
    RequestConfig(request).configure(tab)
    pass_data['table'] = tab
    pass_data['page'] = {'title':'MRIs'}
    return render(request, 'patientdb/table_index.html', pass_data)

@login_required
def pat_index(request):
    pass_data = {}
    qset = Patients.objects.all()
    tab = PatientTable(qset)
    RequestConfig(request).configure(tab)
    pass_data['table'] = tab
    pass_data['page'] = {'title':'Patients'}
    return render(request, 'patientdb/table_index.html', pass_data)

@login_required
def pat_view(request, id):
    pass_data = {}
    qset = Patients.objects.get(pk=id)
    pass_data['patient'] = qset
    tab = DisorderTable(qset.disorders_set.all())
    RequestConfig(request).configure(tab)
    pass_data['disorder_table'] = tab

    tab = MriTable(qset.mris_set.all())
    RequestConfig(request).configure(tab)
    pass_data['mri_table'] = tab

    return render(request, 'patientdb/pat_view.html', pass_data)

@login_required
def proj_index(request):
    pass_data = {}
    qset = Projects.objects.all()
    tab = ProjectTable(qset)
    RequestConfig(request).configure(tab)
    pass_data['table'] = tab
    pass_data['page'] = {'title':'Projects'}
    return render(request, 'patientdb/table_index.html', pass_data)

@login_required
def proj_view(request, id):
    pass_data = {}
    qset = Projects.objects.get(pk=id)
    pass_data['data'] = qset
    tab = PatientTable(qset.subjects.all())
    RequestConfig(request).configure(tab)
    pass_data['table'] = tab
    return render(request, 'patientdb/proj_view.html', pass_data)

@login_required
def mri_view(request, id):
    pass_data = {}
    qset = Mris.objects.get(pk=id)
    pass_data['data'] = qset
    return render(request, 'patientdb/mri_view.html', pass_data)

