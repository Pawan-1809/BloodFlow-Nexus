from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	class Roles(models.TextChoices):
		DONOR = 'donor', 'Donor'
		RECEIVER = 'receiver', 'Blood Receiver'
		HOSPITAL = 'hospital', 'Hospital/Blood Bank'
		ADMIN = 'admin', 'Admin'

	role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.DONOR)
	phone = models.CharField(max_length=20, blank=True)
	city = models.CharField(max_length=120, blank=True)
	state = models.CharField(max_length=120, blank=True)
	address = models.CharField(max_length=255, blank=True)

	def __str__(self) -> str:
		return f"{self.username} ({self.get_role_display()})"


class UserDocument(models.Model):
	class DocTypes(models.TextChoices):
		ID = 'id', 'Government ID'
		MEDICAL = 'medical', 'Medical Document'

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
	doc_type = models.CharField(max_length=20, choices=DocTypes.choices)
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return f"{self.user.username} - {self.get_doc_type_display()}"
