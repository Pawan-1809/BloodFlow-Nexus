from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone


class DonorProfile(models.Model):
	BLOOD_GROUPS = [
		('A+', 'A+'), ('A-', 'A-'),
		('B+', 'B+'), ('B-', 'B-'),
		('AB+', 'AB+'), ('AB-', 'AB-'),
		('O+', 'O+'), ('O-', 'O-'),
	]

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donor_profile')
	blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
	age = models.PositiveIntegerField()
	weight = models.PositiveIntegerField()
	health_condition = models.CharField(max_length=255, blank=True)
	last_donation_date = models.DateField(null=True, blank=True)
	is_available = models.BooleanField(default=True)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

	def eligible_to_donate(self, gap_days: int = 90) -> bool:
		if not self.last_donation_date:
			return True
		next_date = self.last_donation_date + timedelta(days=gap_days)
		return timezone.now().date() >= next_date

	def save(self, *args, **kwargs):
		gap_days = getattr(settings, 'DONATION_GAP_DAYS', 90)
		if self.last_donation_date:
			self.is_available = self.eligible_to_donate(gap_days=gap_days)
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return f"{self.user.username} - {self.blood_group}"


class Donation(models.Model):
	donor = models.ForeignKey(DonorProfile, on_delete=models.CASCADE, related_name='donations')
	hospital_name = models.CharField(max_length=255)
	patient_name = models.CharField(max_length=255, blank=True)
	date = models.DateField(default=timezone.now)
	units = models.PositiveIntegerField(default=1)
	notes = models.TextField(blank=True)

	def __str__(self) -> str:
		return f"{self.donor.user.username} - {self.date}"
