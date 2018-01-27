from rest_framework import serializers
from .models import Patient, Appointment

class PatientSerializer(serializers.ModelSerializer):

    class Meta:

        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=['%d/%m/%Y'], format='%d/%m/%Y')

    class Meta:

        model = Appointment
        fields = '__all__'