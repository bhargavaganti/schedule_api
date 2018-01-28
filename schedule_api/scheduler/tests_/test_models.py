from django.test import TestCase
from model_mommy import mommy
from django.utils.timesince import datetime
from scheduler.models import Patient, Appointment
from scheduler.serializers import PatientSerializer

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

class TestAppointment(TestCase):

    def setUp(self):
        self.appointment = mommy.make(Appointment, date=datetime.date.today())

    def test_appointment_creation(self):
        self.assertTrue(isinstance(self.appointment, Appointment))

''' API Tests '''
class TestDRFScheduler(TestCase):
    pass