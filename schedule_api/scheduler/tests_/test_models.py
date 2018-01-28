from django.test import TestCase, Client
from model_mommy import mommy
from django.utils.timesince import datetime
from scheduler.models import Patient, Appointment
from scheduler.serializers import PatientSerializer

from rest_framework.test import APIClient
from rest_framework import status
import json

''' Basics tests '''
class TestPatient(TestCase):

    def setUp(self):
        self.patient = mommy.make(Patient, name='Jorge')
        patient = Patient.objects.create(
            name='teste', id_number='0001', age='35').save()
        PatientSerializer(patient, many=True)

    def test_patient_creation(self):
        self.assertTrue(isinstance(self.patient, Patient))
        self.assertEquals(self.patient.__str__(), self.patient.name)
        self.assertEquals(
            str(Patient.objects.get(name='teste')) , 'teste')
        Patient.objects.filter(name='teste').delete()

class TestAppointment(TestCase):

    def setUp(self):
        self.appointment = mommy.make(Appointment, date=datetime.date.today())

    def test_appointment_creation(self):
        self.assertTrue(isinstance(self.appointment, Appointment))

''' According to documentation @ DRF guides
    /api-guide/testing/#apiclient       '''
class TestSchedulerAPI(TestCase):

    def setUp(self):
        client = APIClient()

        # for patient test
        client.post('/patients/',
            {'name': 'Test Patient1', 'age': '30', 'id_number': '1'})


    ''' Methods for patients '''
    def test_create_patient(self):
        '''create a new patient '''
        response = self.client.post(
            path='/patients/',
            data={'name': 'Test Patient2', 'age': '31', 'id_number': '2'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
