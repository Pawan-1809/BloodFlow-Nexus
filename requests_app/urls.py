from django.urls import path

from . import views

app_name = 'requests_app'

urlpatterns = [
    path('new/', views.create_request, name='create'),
    path('mine/', views.my_requests, name='my_requests'),
    path('all/', views.all_requests, name='all_requests'),
]
