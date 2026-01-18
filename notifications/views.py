from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Notification


@login_required
def inbox(request):
	notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
	return render(request, 'notifications/inbox.html', {'notifications': notifications})
