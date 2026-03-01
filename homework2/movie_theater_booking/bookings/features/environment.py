import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_theater_booking.settings')
django.setup()

from django.test.runner import DiscoverRunner
from django.core.management import call_command

runner = DiscoverRunner(verbosity=0)
old_db = None

def before_all(context):
    global old_db
    from django.test.utils import setup_test_environment
    setup_test_environment()
    old_db = runner.setup_databases()
    # Run migrations on the test database
    call_command('migrate', verbosity=0)

def after_all(context):
    global old_db
    if old_db is not None:
        runner.teardown_databases(old_db)

def before_scenario(context, scenario):
    call_command('loaddata', 'bookings/fixtures/test_data.json', verbosity=0)

def after_scenario(context, scenario):
    from django.contrib.auth.models import User
    from bookings.models import Movie, Seat, Booking
    Booking.objects.all().delete()
    Seat.objects.all().delete()
    Movie.objects.all().delete()
    User.objects.all().delete()
