from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'



class ServiceForm(forms.ModelForm):
    class Meta:
        model=Service
        fields='__all__'



class SlotForm(forms.ModelForm):
    class Meta:
        model=TimeSlot
        fields='__all__'