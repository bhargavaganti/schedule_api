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

'''
According to documentation @ DRF guides
/api-guide/testing/#apiclient
'''
class TestSchedulerAPI(TestCase):

    def setUp(self):
        client = APIClient()

        # for patient test
        client.post('/patients/',
            {'name': 'Test Patient1', 'age': '30', 'id_number': '1'})
        # for appointment test
        client.post('/appointments/',
            {"date": "01/03/2018", "start_time": "08:00",
             "end_time": "09:00", "procedure": "Consulta", "patient": 1})


    ''' Methods for patients '''
    def test_create_patient(self):
        '''create a new patient '''
        response = self.client.post(
            path='/patients/',
            data={'name': 'Test Patient2', 'age': '31', 'id_number': '2'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_patient_duplicate_id(self):
        '''create a duplicate patient '''
        response = self.client.post(
            path='/patients/',
            data={'name': 'Test Patient1', 'age': '30', 'id_number': '1'}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patient_list(self):
        ''' request all patients '''
        response = self.client.get('/patients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_patient_detail_onlist(self):
        ''' request patient 1 '''
        response = self.client.get('/patient/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patient_detail_nonlist(self):
        ''' request patient 2 '''
        response = self.client.get('/patient/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    ''' Methods for appointments '''
    def test_create_valid_appointment(self):
        '''create a new appointment out of the period of 1  '''
        response = self.client.post(
            path='/appointments/',
            data={"date": "01/03/2018", "start_time": "09:10",
                  "end_time": "10:00", "procedure": "Consulta", "patient": 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_nvalid_appointments(self):
        '''create a new appointment but overlaping periods '''
        response = self.client.post(
            path='/appointments/',
            data={"date": "01/03/2018", "start_time": "07:00",
                  "end_time": "09:00", "procedure": "Consulta", "patient": 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

