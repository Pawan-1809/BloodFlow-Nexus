from django.contrib import admin

from .models import BloodStock, DonationSchedule, HospitalProfile


@admin.register(HospitalProfile)
class HospitalProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'city', 'phone')


@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):
	list_display = ('hospital', 'blood_group', 'units', 'updated_at')
	list_filter = ('blood_group',)


@admin.register(DonationSchedule)
class DonationScheduleAdmin(admin.ModelAdmin):
	list_display = ('hospital', 'donor_name', 'scheduled_at', 'status')
	list_filter = ('status',)
