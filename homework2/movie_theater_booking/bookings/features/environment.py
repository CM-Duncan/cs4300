import django
import os

def before_all(context):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_theater_booking.settings')
    django.setup()

def before_scenario(context, scenario):
    from django.test.utils import setup_test_environment
    setup_test_environment()
