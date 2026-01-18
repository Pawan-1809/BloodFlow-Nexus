from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import BloodStockForm, DonationScheduleForm, HospitalProfileForm
from .models import BloodStock, DonationSchedule, HospitalProfile


@login_required
def hospital_profile(request):
	profile, _ = HospitalProfile.objects.get_or_create(
		user=request.user,
		defaults={'name': request.user.username, 'address': 'Update address', 'city': request.user.city or 'City'},
	)

	if request.method == 'POST':
		form = HospitalProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'Hospital profile updated.')
			return redirect('hospitals:profile')
	else:
		form = HospitalProfileForm(instance=profile)

	return render(request, 'hospitals/profile.html', {'form': form, 'profile': profile})


@login_required
def stock_list(request):
	profile = getattr(request.user, 'hospital_profile', None)
	stocks = BloodStock.objects.filter(hospital=profile) if profile else []
	return render(request, 'hospitals/stocks.html', {'stocks': stocks})


@login_required
def stock_add(request):
	profile = getattr(request.user, 'hospital_profile', None)
	if not profile:
		return redirect('hospitals:profile')

	if request.method == 'POST':
		form = BloodStockForm(request.POST)
		if form.is_valid():
			stock = form.save(commit=False)
			stock.hospital = profile
			stock.save()
			messages.success(request, 'Blood stock updated.')
			return redirect('hospitals:stocks')
	else:
		form = BloodStockForm()

	return render(request, 'hospitals/stock_add.html', {'form': form})


@login_required
def schedule_list(request):
	profile = getattr(request.user, 'hospital_profile', None)
	schedules = DonationSchedule.objects.filter(hospital=profile) if profile else []
	return render(request, 'hospitals/schedules.html', {'schedules': schedules})


@login_required
def schedule_add(request):
	profile = getattr(request.user, 'hospital_profile', None)
	if not profile:
		return redirect('hospitals:profile')

	if request.method == 'POST':
		form = DonationScheduleForm(request.POST)
		if form.is_valid():
			schedule = form.save(commit=False)
			schedule.hospital = profile
			schedule.save()
			messages.success(request, 'Donation schedule created.')
			return redirect('hospitals:schedules')
	else:
		form = DonationScheduleForm()

	return render(request, 'hospitals/schedule_add.html', {'form': form})
