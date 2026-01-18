from django.conf import settings
from django.db import models


class HospitalProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hospital_profile')
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=120)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

	def __str__(self) -> str:
		return self.name


class BloodStock(models.Model):
	BLOOD_GROUPS = [
		('A+', 'A+'), ('A-', 'A-'),
		('B+', 'B+'), ('B-', 'B-'),
		('AB+', 'AB+'), ('AB-', 'AB-'),
		('O+', 'O+'), ('O-', 'O-'),
	]

	hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE, related_name='stocks')
	blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
	units = models.PositiveIntegerField(default=0)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('hospital', 'blood_group')

	def __str__(self) -> str:
		return f"{self.hospital.name} - {self.blood_group}"


class DonationSchedule(models.Model):
	STATUS = [
		('scheduled', 'Scheduled'),
		('completed', 'Completed'),
		('cancelled', 'Cancelled'),
	]

	hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE, related_name='schedules')
	donor_name = models.CharField(max_length=255)
	scheduled_at = models.DateTimeField()
	status = models.CharField(max_length=20, choices=STATUS, default='scheduled')

	def __str__(self) -> str:
		return f"{self.hospital.name} - {self.scheduled_at}"
