from django import forms
from .models import user


class PatientRegistration(forms.ModelForm):
    class Meta:
        model = user
        fields = ['Patient_name', 'Patient_address', 'Phone_No']
        widgets = {
            'Patient_address': forms.Textarea(attrs={'class': 'form-control'}),
        }
