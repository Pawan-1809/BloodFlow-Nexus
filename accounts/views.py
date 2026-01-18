from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, RegistrationForm


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Account created successfully.')
			return redirect('dashboard:home')
	else:
		form = RegistrationForm()

	return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Profile updated successfully.')
			return redirect('accounts:profile')
	else:
		form = ProfileForm(instance=request.user)

	return render(request, 'accounts/profile.html', {'form': form})
