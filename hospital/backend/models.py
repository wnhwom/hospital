from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)




class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length =10, choices=[('Male','Male'), ('Female', 'Female')])
    birth_date = models.DateField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)



class Service(models.Model):
    name = models.CharField(max_length=100)
    type_of_service = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name



class Visit(models.Model):
    PLANNED = 'PLANNED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (PLANNED,PLANNED),
        (COMPLETED,COMPLETED),
        (CANCELLED,CANCELLED)
     ]


    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visits')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.doctor.full_name} - {self.patient.full_name} - {self.visit_date}'






