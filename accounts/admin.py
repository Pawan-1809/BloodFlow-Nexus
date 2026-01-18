from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserDocument


@admin.register(User)
class CustomUserAdmin(UserAdmin):
	fieldsets = UserAdmin.fieldsets + (
		('Additional Info', {'fields': ('role', 'phone', 'city', 'state', 'address')}),
	)
	list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
	list_filter = ('role', 'is_staff', 'is_active')


@admin.register(UserDocument)
class UserDocumentAdmin(admin.ModelAdmin):
	list_display = ('user', 'doc_type', 'uploaded_at')
