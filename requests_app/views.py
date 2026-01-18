from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import BloodRequestForm
from .models import BloodRequest
from donors.models import DonorProfile
from notifications.models import Notification


@login_required
def create_request(request):
	if request.method == 'POST':
		form = BloodRequestForm(request.POST)
		if form.is_valid():
			blood_request = form.save(commit=False)
			blood_request.requester = request.user
			blood_request.save()

			matching_donors = DonorProfile.objects.filter(
				blood_group=blood_request.blood_group,
				is_available=True,
			).select_related('user')

			notifications = [
				Notification(
					user=donor.user,
					title='Matching blood request',
					message=(
						f"Urgent request for {blood_request.blood_group} at "
						f"{blood_request.hospital_location}."
					),
					category=blood_request.urgency,
				)
				for donor in matching_donors
			]
			Notification.objects.bulk_create(notifications)
			messages.success(request, 'Blood request submitted successfully.')
			return redirect('requests_app:my_requests')
	else:
		form = BloodRequestForm()

	return render(request, 'requests/create.html', {'form': form})


@login_required
def my_requests(request):
	requests = BloodRequest.objects.filter(requester=request.user).order_by('-created_at')
	return render(request, 'requests/my_requests.html', {'requests': requests})


@login_required
def all_requests(request):
	requests = BloodRequest.objects.select_related('requester', 'hospital').order_by('-created_at')
	return render(request, 'requests/all_requests.html', {'requests': requests})
