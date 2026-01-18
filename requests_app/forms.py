from django import forms

from .models import BloodRequest


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = (
            'blood_group',
            'quantity_units',
            'urgency',
            'hospital_location',
            'hospital',
        )
