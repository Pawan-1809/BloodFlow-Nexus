from django.db.models import Count
from django.shortcuts import render

from donors.models import DonorProfile, Donation
from requests_app.models import BloodRequest


def home(request):
	stats = {
		'donors': DonorProfile.objects.count(),
		'requests': BloodRequest.objects.count(),
		'donations': Donation.objects.count(),
	}
	latest_requests = BloodRequest.objects.order_by('-created_at')[:5]
	return render(request, 'dashboard/home.html', {'stats': stats, 'latest_requests': latest_requests})
