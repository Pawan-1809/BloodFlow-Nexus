from django.conf import settings
from django.db import models

from hospitals.models import HospitalProfile


class BloodRequest(models.Model):
	class Urgency(models.TextChoices):
		NORMAL = 'normal', 'Normal'
		EMERGENCY = 'emergency', 'Emergency'

	class Status(models.TextChoices):
		PENDING = 'pending', 'Pending'
		APPROVED = 'approved', 'Approved'
		COMPLETED = 'completed', 'Completed'
		REJECTED = 'rejected', 'Rejected'

	BLOOD_GROUPS = [
		('A+', 'A+'), ('A-', 'A-'),
		('B+', 'B+'), ('B-', 'B-'),
		('AB+', 'AB+'), ('AB-', 'AB-'),
		('O+', 'O+'), ('O-', 'O-'),
	]

	requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='requests')
	hospital = models.ForeignKey(HospitalProfile, on_delete=models.SET_NULL, null=True, blank=True)
	blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
	quantity_units = models.PositiveIntegerField()
	urgency = models.CharField(max_length=20, choices=Urgency.choices, default=Urgency.NORMAL)
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
	hospital_location = models.CharField(max_length=255)
	assigned_donor = models.CharField(max_length=255, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return f"{self.requester.username} - {self.blood_group}"
