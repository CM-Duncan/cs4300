from django.test import TestCase, Client
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
import datetime

# ---- UNIT TESTS ----

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

    def test_movie_fields(self):
        self.assertEqual(self.movie.title, "Inception")
        self.assertEqual(self.movie.duration, 148)


class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A1")

    def test_seat_str(self):
        self.assertEqual(str(self.seat), "Seat: A1")

    def test_seat_default_not_booked(self):
        self.assertFalse(self.seat.is_booked)


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='pass123'
        )
        self.movie = Movie.objects.create(
            title="The Dark Knight",
            description="Batman vs Joker",
            release_date=datetime.date(2008, 7, 18),
            duration=152
        )
        self.seat = Seat.objects.create(seat_number="B2")
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

    def test_booking_str(self):
        self.assertIn("testuser", str(self.booking))
        self.assertIn("The Dark Knight", str(self.booking))

    def test_booking_links_user_movie_seat(self):
        self.assertEqual(self.booking.user, self.user)
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)


# ---- INTEGRATION TESTS ----

class MovieAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(
            title="Interstellar",
            description="Space exploration",
            release_date=datetime.date(2014, 11, 7),
            duration=169
        )

    def test_api_movie_list_status(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)

    def test_api_movie_list_contains_movie(self):
        response = self.client.get('/api/movies/')
        self.assertContains(response, "Interstellar")

    def test_api_seats_list_status(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, 200)


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='pass123'
        )
        self.movie = Movie.objects.create(
            title="Inception",
            description="Dreams",
            release_date=datetime.date(2010, 7, 16),
            duration=148
        )
        self.seat = Seat.objects.create(seat_number="A1")

    def test_movie_list_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_booking_history_requires_login(self):
        response = self.client.get('/bookings/history/')
        self.assertEqual(response.status_code, 302)  # redirects to login

    def test_booking_history_logged_in(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.get('/bookings/history/')
        self.assertEqual(response.status_code, 200)

    def test_book_seat_post(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.post(
            f'/book/{self.movie.id}/',
            {'seat_id': self.seat.id}
        )
        self.assertEqual(response.status_code, 302)  # redirects after booking
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.is_booked)
