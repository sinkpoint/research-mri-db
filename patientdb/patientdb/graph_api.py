from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from patientdb.models import *
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        'patient_ages': reverse('patient_age_dist', request=request, format=format)
    })

@api_view(['GET'])
def patient_age_dist(request, format=None):
    qset = Patients.objects.all()
    ages = [i.age_added for i in qset]
    print ages

    import numpy as np
    bins = range(0,100,5)
    hist, edges = np.histogram(ages, bins)

    return Response({'hist':hist, 'edges':edges})




