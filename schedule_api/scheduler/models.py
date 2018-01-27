from django.db import models

class Patient(models.Model):

    class Meta:

        db_table = 'patient'

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    id_number = models.IntegerField()

    def __str__(self):
        return self.name