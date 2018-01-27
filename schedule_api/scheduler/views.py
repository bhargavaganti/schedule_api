from rest_framework import generics, status
from .models import Patient, Appointment
from .serializers import PatientSerializer, AppointmentSerializer

''' Return a list of all patients with GET
    This class can also create a new Patient with POST '''
class PatientList(generics.ListCreateAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

''' Return a list of described patient with GET
    This method can also update a  Patient with PUT 
    or delete with DELETE '''
class PatientDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

''' Return a list of all appointments with GET
    This class can also create a new appointment with POST '''
class AppointmentList(generics.ListCreateAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

''' Return a list of described appointments with GET
    This method can also update an appointment with PUT 
    or delete with DELETE '''
class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer