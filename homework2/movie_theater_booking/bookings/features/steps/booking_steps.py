from behave import given, when, then
from django.test import Client
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
import datetime

@given('the database has movies')
def step_database_has_movies(context):
    context.movie = Movie.objects.create(
        title="Test Movie",
        description="A test movie",
        release_date=datetime.date.today(),
        duration=120
    )

@when('I visit the movie list page')
def step_visit_movie_list(context):
    context.client = Client()
    context.response = context.client.get('/')

@then('I should see a list of movies')
def step_see_movie_list(context):
    assert context.response.status_code == 200
    assert b"Test Movie" in context.response.content

@given('I am logged in')
def step_logged_in(context):
    context.client = Client()
    context.user = User.objects.create_user(
        username='testuser',
        password='testpass123'
    )
    context.client.login(username='testuser', password='testpass123')
    context.movie = Movie.objects.create(
        title="Test Movie",
        description="A test movie",
        release_date=datetime.date.today(),
        duration=120
    )

@given('there is an available seat')
def step_available_seat(context):
    context.seat = Seat.objects.create(
        seat_number="A1",
        is_booked=False
    )

@when('I book the seat for a movie')
def step_book_seat(context):
    context.response = context.client.post(
        f'/book/{context.movie.id}/',
        {'seat_id': context.seat.id}
    )

@then('the seat should be marked as booked')
def step_seat_is_booked(context):
    context.seat.refresh_from_db()
    assert context.seat.is_booked == True

@given('I have an existing booking')
def step_existing_booking(context):
    seat = Seat.objects.create(seat_number="B1", is_booked=True)
    context.booking = Booking.objects.create(
        movie=context.movie,
        seat=seat,
        user=context.user
    )

@when('I visit the booking history page')
def step_visit_booking_history(context):
    context.response = context.client.get('/bookings/history/')

@then('I should see my booking')
def step_see_booking(context):
    assert context.response.status_code == 200
    assert b"Test Movie" in context.response.content
