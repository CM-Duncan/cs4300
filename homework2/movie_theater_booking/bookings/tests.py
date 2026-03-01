"Caroline Duncan, 2/28/26,  "
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
import datetime

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date=datetime.date(2010, 7, 16),
            duration=148
        )

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Inception")

class BookingIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.movie = Movie.objects.create(title="Test", description="desc",
                                          release_date=datetime.date.today(), duration=90)
        self.seat = Seat.objects.create(seat_number="A1")

    def test_api_movie_list(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)

    def test_booking_requires_login(self):
        response = self.client.get('/bookings/history/')
        self.assertEqual(response.status_code, 302)  # redirect to login
