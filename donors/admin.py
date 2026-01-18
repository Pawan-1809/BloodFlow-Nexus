from django.contrib import admin

from .models import DonorProfile, Donation


@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'blood_group', 'is_available', 'last_donation_date')
	list_filter = ('blood_group', 'is_available')


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
	list_display = ('donor', 'hospital_name', 'date', 'units')
