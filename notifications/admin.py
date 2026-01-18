from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ('user', 'title', 'category', 'is_read', 'created_at')
	list_filter = ('category', 'is_read')
