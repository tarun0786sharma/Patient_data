from django.forms import ModelForm
from django import forms
from .models import *


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'