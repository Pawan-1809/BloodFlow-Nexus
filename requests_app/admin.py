from django.contrib import admin

from .models import BloodRequest


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
	list_display = ('requester', 'blood_group', 'quantity_units', 'urgency', 'status', 'created_at')
	list_filter = ('urgency', 'status', 'blood_group')
