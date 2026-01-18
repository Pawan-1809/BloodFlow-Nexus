import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import DonorProfileForm, DonationForm
from .models import DonorProfile, Donation


@login_required
def donor_profile(request):
	profile, _ = DonorProfile.objects.get_or_create(user=request.user, defaults={
		'blood_group': 'O+',
		'age': 18,
		'weight': 50,
	})

	if request.method == 'POST':
		form = DonorProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'Donor profile updated.')
			return redirect('donors:profile')
	else:
		form = DonorProfileForm(instance=profile)

	return render(request, 'donors/profile.html', {'form': form, 'profile': profile})


@login_required
def donor_search(request):
	qs = DonorProfile.objects.select_related('user').all()
	blood_group = request.GET.get('blood_group')
	city = request.GET.get('city')
	availability = request.GET.get('availability')

	if blood_group:
		qs = qs.filter(blood_group=blood_group)
	if city:
		qs = qs.filter(user__city__icontains=city)
	if availability in {'available', 'not_available'}:
		qs = qs.filter(is_available=(availability == 'available'))

	donor_points = [
		{
			'name': donor.user.username,
			'blood_group': donor.blood_group,
			'city': donor.user.city,
			'lat': float(donor.latitude),
			'lng': float(donor.longitude),
		}
		for donor in qs
		if donor.latitude is not None and donor.longitude is not None
	]

	return render(
		request,
		'donors/search.html',
		{
			'donors': qs,
			'donor_points': json.dumps(donor_points),
		},
	)


@login_required
def donation_history(request):
	profile = getattr(request.user, 'donor_profile', None)
	donations = Donation.objects.filter(donor=profile).order_by('-date') if profile else []
	return render(request, 'donors/history.html', {'donations': donations})


@login_required
def add_donation(request):
	profile = getattr(request.user, 'donor_profile', None)
	if not profile:
		return redirect('donors:profile')

	if request.method == 'POST':
		form = DonationForm(request.POST)
		if form.is_valid():
			donation = form.save(commit=False)
			donation.donor = profile
			donation.save()
			messages.success(request, 'Donation recorded successfully.')
			return redirect('donors:history')
	else:
		form = DonationForm()

	return render(request, 'donors/add_donation.html', {'form': form})
