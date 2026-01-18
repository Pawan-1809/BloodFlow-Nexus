# Blood Donation Management App

A modern Django-based blood donation management platform with donor discovery, request tracking, hospital inventory, and in-app notifications.

## Features

- Role-based users: donors, receivers, hospitals, admins
- Donor availability and donation history
- Blood request lifecycle (pending, approved, completed)
- Hospital stock management and scheduling
- Notifications hub
- Modern UI with Tailwind CDN + GSAP/ScrollReveal transitions

## Setup

1. Create and activate a Python environment (already configured in this workspace).
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Apply migrations:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
4. Create admin user:
   - `python manage.py createsuperuser`
5. Run the server:
   - `python manage.py runserver`

## Notes

- Uses SQLite by default.
- Static files are under `static/` and templates under `templates/`.
