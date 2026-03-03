Caroline Duncan
Created: 3/2/26
CS 4300 

## Project Overiew:
A RESTful Movie Theater Booking Application built with Python and Django. Users can view movie listings, book seats, and check their booking history.

## Project Structure
```
homework2/
└── movie_theater_booking/
    ├── manage.py
    ├── build.sh                        # Render deployment script
    ├── requirements.txt
    ├── movie_theater_booking/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    └── bookings/
        ├── models.py                   # Movie, Seat, Booking models
        ├── serializers.py              # DRF serializers
        ├── views.py                    # ViewSets + template views
        ├── urls.py                     # API routes
        ├── template_urls.py            # UI routes
        ├── admin.py                    # Admin panel registration
        ├── tests.py                    # Unit & integration tests
        ├── fixtures/
        │   └── test_data.json          # Sample data loaded on deployment
        ├── templates/bookings/
        │   ├── base.html               # Base Bootstrap template
        │   ├── login.html              # Login page
        │   ├── movie_list.html         # Movie listings page
        │   ├── seat_booking.html       # Seat booking page
        │   └── booking_history.html    # Booking history page
        └── features/
            ├── booking.feature         # BDD feature file
            ├── environment.py          # Behave Django setup
            └── steps/
                └── booking_steps.py    # BDD step definitions
```

## Setup Instructions:

### Option 1: Run on Render
1. Run live site using link: **https://movie-theater-booking-a04d.onrender.com**
2. Login using credentials below.

### Option 2: Run on DevEdu
1. Activate virtual environment
'source ~/cs4300/homework2/homework2_env/bin activate'
2. Navigate to project:
'cd ~/cs4300/homework2/movie_theater_booking'
3. Start server: 
'python manage.py runserver 0.0.0.0:3000'
4. Continue by using step 2 from option 1

## Login Credentials:
For Admin: 
1. Username: admin
Password: student
For Regular users: 
2. Username: student
Password: password123

## API Endpoints:
- GET/POST: '/api/movies/' , List all movies/create a movie
- GET/PUT/DELETE: '/api/movies/<id>/' , Retrieve, update a movie
- GET/POST: '/api/seats/' , Lists all seats/create a seat
- GET/PUT/DELETE: '/api/seats/<id>/' , Retrieve, update a seat
- GET/POST: List all user booking/create a booking
- GET/PUT/DELETE: '/api/bookings/<id>/' , Retrieve, update a booking

## UI Pages:
- Movie List: '/', View all available movies
- Seat Booking: '/book/<movie_id>', Book seat for a movie
- Booking History: '/bookings/history/' , View past bookings
- Login: '/login/', Log into account
- Logout: '/logout/', Log out
- Admin Panel: '/admin/', Manages all data

## Running Tests:
### Unit/Integration Tests:
'python manage.py test'
- Expected output: 13 passing tests

### BDD Tests
'DJANGO_SETTINGS_MODULE=movie_theater_booking.settings behave bookings/features/'
- Expected output: 2 scenarios, 7 steps passing

## Deploying:
Website is deployed on Render
### Settings
- Build Command: './build.sh'
- Start Command: 'gunicorn movie_theater_booking.wsgi:application'
- Runtime: Python 3.12
### Notes: 
- Sample movie and seat data is automatically loaded on every deploy via './build.sh'
- 'CSRF_TRUSTED_ORIGINS' must include your domain to allow login to work
- SQLite is used for the database, data resets every Render redeploy

## Known Configurations:
In 'settings.py' make sure these are set:
1. 'ALLOWED_HOSTS = ['movie-theater-booking-a04d.onrender.com', 'localhost', '127.0.0.1', '*']'
2. CSRF_TRUSTED_ORIGINS = [
    'https://movie-theater-booking-a04d.onrender.com',
    'https://app-caroline-21.devedu.io',
    'https://*.devedu.io',
]

## AI Usage
AI (Claude) was used to create the templates (base,booking_history,login,movie_list and seat_booking.html). AI was also used to fix any programming and website issues, as well as creating the project structure for this readme. 

## Dependencies
- Django
- djangorestframework
- gunicorn
- whitenoise
- behave
- django-behave