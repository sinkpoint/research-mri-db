from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
import graph_api

admin.autodiscover()

router = routers.DefaultRouter()


urlpatterns = [
    # Examples:
    # url(r'^$', 'patientdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/?$', graph_api.api_root),
    url(r'^api/patient_ages/?$', 'patientdb.graph_api.patient_age_dist', name='patient_age_dist'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^/?$', 'patientdb.views.index', name='dash'),
    url(r'^projects/?$', 'patientdb.views.proj_index', name='projects'),
    url(r'^projects/([0-9]+)/?$', 'patientdb.views.proj_view', name='proj_view'),
    url(r'^patients/?$', 'patientdb.views.pat_index', name='patients'),
    url(r'^patients/([0-9]+)/?$', 'patientdb.views.pat_view', name='pat_view'),
    url(r'^mris/?$', 'patientdb.views.mri_index', name='mris'),
    url(r'^mris/([0-9]+)/?$', 'patientdb.views.mri_view', name='mri_view'),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^login/?', 'patientdb.views.login'),
    url(r'^accounts/?', include('allauth.urls')),
]

from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve as serve_static
if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', never_cache(serve_static)),
    ]
