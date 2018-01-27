from rest_framework import generics
from .models import Patient, Appointment
from .serializers import PatientSerializer, AppointmentSerializer

class PatientList(generics.ListCreateAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentList(generics.ListCreateAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer