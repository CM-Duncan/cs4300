from behave import given, when, then

@given('the database has movies')
def step_database_has_movies(context):
    # Data already loaded from fixture
    from bookings.models import Movie
    context.movie = Movie.objects.get(pk=1)

@when('I visit the movie list page')
def step_visit_movie_list(context):
    from django.test import Client
    context.client = Client()
    context.response = context.client.get('/')

@then('I should see a list of movies')
def step_see_movie_list(context):
    assert context.response.status_code == 200
    assert b"Inception" in context.response.content

@given('I am logged in')
def step_logged_in(context):
    from django.test import Client
    from django.contrib.auth.models import User
    from bookings.models import Movie
    context.client = Client()
    # Create user directly so we know the password
    context.user = User.objects.create_user(
        username='behaveuser',
        password='testpass123'
    )
    context.client.login(username='behaveuser', password='testpass123')
    context.movie = Movie.objects.get(pk=1)

@given('there is an available seat')
def step_available_seat(context):
    from bookings.models import Seat
    context.seat = Seat.objects.get(pk=1)  # A1 is unbooked in fixture

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
    from bookings.models import Booking
    # Booking pk=1 already exists in fixture
    context.booking = Booking.objects.get(pk=1)

@when('I visit the booking history page')
def step_visit_booking_history(context):
    context.response = context.client.get('/bookings/history/')

@then('I should see my booking')
def step_see_booking(context):
    assert context.response.status_code == 200
    assert b"Inception" in context.response.content
