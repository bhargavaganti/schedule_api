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

    ''' Check POST method for consistences '''
    def post(self, request, *args, **kwargs):

        appointment = AppointmentSerializer(data=request.data)

        if (appointment.is_valid() == True):
            date = appointment.validated_data['date']
            start_time = appointment.validated_data['start_time']
            end_time = appointment.validated_data['end_time']

            if start_time >= end_time:
                return Response({'error': 'Start time must be earlier than end time.'},
                    status=status.HTTP_400_BAD_REQUEST)

        return self.create(request, *args, **kwargs)

''' Return a list of described appointments with GET
    This method can also update an appointment with PUT 
    or delete with DELETE '''
class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer