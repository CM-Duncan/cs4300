"Caroline Duncan, 2/28/26, defines three URL routes for the bookings app, mapping the movie list page, a seat booking page "
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('book/<int:movie_id>/', views.seat_booking, name='book_seat'),
    path('bookings/history/', views.booking_history, name='booking_history'),
]
