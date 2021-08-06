from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Patients(models.Model):
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    gender = models.CharField(max_length=200, null=True, blank=True, choices=gender_choice, default='Pending')
    age = models.IntegerField(max_length=200, default=1, validators=[MaxValueValidator(120), MinValueValidator(1)])
    disease = models.CharField(max_length=20)
    doctor_name = models.CharField(max_length=20)
    doctor_fees = models.CharField(max_length=20, default=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first + " " + self.last

    class Meta:
        verbose_name_plural = "Patient Information"
