"""
WSGI config for blood_donation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blood_donation.settings')

application = get_wsgi_application()

if os.getenv('VERCEL'):
	try:
		from django.core.management import call_command

		call_command('migrate', interactive=False, verbosity=0)
	except Exception:
		pass
