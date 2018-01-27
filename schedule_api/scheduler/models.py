from django.db import models

class Patient(models.Model):

    class Meta:

        db_table = 'patient'

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    id_number = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    class Meta:

        db_table = 'scheduling'

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='appointment')
    procedure = models.CharField(max_length=255)

    def __str__(self):
        return str('Appointment for %s at %s %s %s' % (self.patient,
                                                       self.date,
                                                       self.start_time,
                                                       self.end_time,
                                                       self.procedure))


