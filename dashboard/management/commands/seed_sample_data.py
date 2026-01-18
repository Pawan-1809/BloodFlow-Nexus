from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from accounts.models import User
from donors.models import DonorProfile, Donation
from hospitals.models import HospitalProfile, BloodStock, DonationSchedule
from notifications.models import Notification
from requests_app.models import BloodRequest


class Command(BaseCommand):
    help = 'Seed the database with sample data for demo/testing.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding sample data...')

        donors = [
            {'username': 'donor_ali', 'email': 'ali.donor@example.com', 'city': 'Delhi', 'blood_group': 'O+'},
            {'username': 'donor_maya', 'email': 'maya.donor@example.com', 'city': 'Mumbai', 'blood_group': 'A+'},
            {'username': 'donor_ravi', 'email': 'ravi.donor@example.com', 'city': 'Bengaluru', 'blood_group': 'B+'},
            {'username': 'donor_sana', 'email': 'sana.donor@example.com', 'city': 'Chennai', 'blood_group': 'AB+'},
        ]

        receivers = [
            {'username': 'receiver_jay', 'email': 'jay.receiver@example.com', 'city': 'Delhi'},
            {'username': 'receiver_tara', 'email': 'tara.receiver@example.com', 'city': 'Mumbai'},
        ]

        hospitals = [
            {'username': 'hospital_redline', 'email': 'contact@redline.org', 'name': 'Redline Blood Bank', 'city': 'Delhi'},
            {'username': 'hospital_carebridge', 'email': 'care@carebridge.org', 'name': 'CareBridge Hospital', 'city': 'Mumbai'},
        ]

        default_password = 'Demo@1234'

        for donor in donors:
            user, created = User.objects.get_or_create(
                username=donor['username'],
                defaults={
                    'email': donor['email'],
                    'role': User.Roles.DONOR,
                    'city': donor['city'],
                },
            )
            if created:
                user.set_password(default_password)
                user.save()
            profile, _ = DonorProfile.objects.get_or_create(
                user=user,
                defaults={
                    'blood_group': donor['blood_group'],
                    'age': 25,
                    'weight': 70,
                    'last_donation_date': date.today() - timedelta(days=120),
                    'is_available': True,
                },
            )
            Donation.objects.get_or_create(
                donor=profile,
                hospital_name='Redline Blood Bank',
                date=date.today() - timedelta(days=90),
                defaults={'units': 1, 'patient_name': 'Demo Patient'},
            )

        for receiver in receivers:
            user, created = User.objects.get_or_create(
                username=receiver['username'],
                defaults={
                    'email': receiver['email'],
                    'role': User.Roles.RECEIVER,
                    'city': receiver['city'],
                },
            )
            if created:
                user.set_password(default_password)
                user.save()

        hospital_profiles = []
        for hospital in hospitals:
            user, created = User.objects.get_or_create(
                username=hospital['username'],
                defaults={
                    'email': hospital['email'],
                    'role': User.Roles.HOSPITAL,
                    'city': hospital['city'],
                },
            )
            if created:
                user.set_password(default_password)
                user.save()
            profile, _ = HospitalProfile.objects.get_or_create(
                user=user,
                defaults={
                    'name': hospital['name'],
                    'city': hospital['city'],
                    'address': f"{hospital['city']} Central Ave",
                },
            )
            hospital_profiles.append(profile)

        for profile in hospital_profiles:
            for group in ['A+', 'A-', 'B+', 'O+']:
                BloodStock.objects.get_or_create(
                    hospital=profile,
                    blood_group=group,
                    defaults={'units': 12},
                )
            DonationSchedule.objects.get_or_create(
                hospital=profile,
                donor_name='Ali Hassan',
                scheduled_at=timezone.now() + timedelta(days=3),
                defaults={'status': 'scheduled'},
            )

        receiver_users = User.objects.filter(role=User.Roles.RECEIVER)
        for receiver in receiver_users:
            BloodRequest.objects.get_or_create(
                requester=receiver,
                blood_group='O+',
                quantity_units=2,
                urgency='emergency',
                hospital_location='Central Hospital, Delhi',
                defaults={'status': 'pending'},
            )

        for user in User.objects.filter(role=User.Roles.DONOR):
            Notification.objects.get_or_create(
                user=user,
                title='New emergency request',
                defaults={
                    'message': 'An emergency request needs your blood type in Delhi.',
                    'category': 'emergency',
                },
            )

        self.stdout.write(self.style.SUCCESS('Sample data created. Login password: Demo@1234'))
