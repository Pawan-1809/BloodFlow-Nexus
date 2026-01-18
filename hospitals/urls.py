from django.urls import path

from . import views

app_name = 'hospitals'

urlpatterns = [
    path('profile/', views.hospital_profile, name='profile'),
    path('stocks/', views.stock_list, name='stocks'),
    path('stocks/new/', views.stock_add, name='stock_add'),
    path('schedules/', views.schedule_list, name='schedules'),
    path('schedules/new/', views.schedule_add, name='schedule_add'),
]
