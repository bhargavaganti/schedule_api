from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^patients/$', views.PatientList.as_view(), name='patient-list'),
    re_path(r'^patient/(?P<pk>[0-9]+)/$', views.PatientDetail.as_view(), name='patient-detail'),
    re_path(r'^appointments/$', views.AppointmentList.as_view(), name='appointment-list'),
    re_path(r'^appointment/(?P<pk>[0-9]+)/$', views.AppointmentDetail.as_view(), name='appointment-detail'),
]
