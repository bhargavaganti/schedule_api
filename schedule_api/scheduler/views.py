from rest_framework import generics, status
from .models import Patient, Appointment
from .serializers import PatientSerializer, AppointmentSerializer
from rest_framework.response import Response

''' Return a list of all patients with GET
    This class can also create a new Patient with POST '''
class PatientList(generics.ListCreateAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

''' Return a list of described patient with GET
    This method can also update a patient with PUT
    or delete with DELETE '''
class PatientDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

''' Return a list of all appointments with GET
    This class can also create a new appointment with POST '''
class AppointmentList(generics.ListCreateAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def consistence_is_ok(self, date, start_time, end_time):
        good_appointment = True
        appointment = Appointment.objects.filter(
            date=date, start_time__lte=start_time).order_by('-start_time')

        if appointment.exists():
            # at least 1 appointment has been found before
            close_appointment = appointment.first()
            # Check if the appointment before overlaps the start time
            if close_appointment.end_time > start_time:
                good_appointment = False

        # get the appointments that start after the requested one
        appointment = Appointment.objects.filter(
            date=date, start_time__gt=start_time).order_by('start_time')

        if appointment.exists():
            # at least 1 appointment has been found after
            close_appointment = appointment.first()
            # if the end time of the requested appointment is later
            # than the start time of the next appointment,
            # it cannot be scheduled
            if end_time > close_appointment.start_time:
                good_appointment = False

        return good_appointment

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

            ''' Here overlaps can be identified for consistence  '''
            if self.consistence_is_ok(date, start_time, end_time):
                return self.create(request, *args, **kwargs)
            else:
                return Response({'error': 'Bad appointment.'}, status=status.HTTP_400_BAD_REQUEST)

''' Return a list of described appointments with GET
    This method can also update an appointment with PUT
    or delete with DELETE '''
class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
