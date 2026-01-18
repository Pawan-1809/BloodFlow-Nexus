from django import forms

from .models import HospitalProfile, BloodStock, DonationSchedule


class HospitalProfileForm(forms.ModelForm):
    class Meta:
        model = HospitalProfile
        fields = ('name', 'phone', 'address', 'city', 'latitude', 'longitude')


class BloodStockForm(forms.ModelForm):
    class Meta:
        model = BloodStock
        fields = ('blood_group', 'units')


class DonationScheduleForm(forms.ModelForm):
    class Meta:
        model = DonationSchedule
        fields = ('donor_name', 'scheduled_at', 'status')
