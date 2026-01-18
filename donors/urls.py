from django.urls import path

from . import views

app_name = 'donors'

urlpatterns = [
    path('profile/', views.donor_profile, name='profile'),
    path('search/', views.donor_search, name='search'),
    path('history/', views.donation_history, name='history'),
    path('donations/new/', views.add_donation, name='add_donation'),
]
