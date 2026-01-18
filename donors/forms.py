from django import forms

from .models import DonorProfile, Donation


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = (
            'blood_group',
            'age',
            'weight',
            'health_condition',
            'last_donation_date',
            'is_available',
            'latitude',
            'longitude',
        )


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('hospital_name', 'patient_name', 'date', 'units', 'notes')
