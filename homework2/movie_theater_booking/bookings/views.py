"Caroline Duncan, 2/28/26, sets up a rest api endpoint that lets authenticated-or-open users perform full CRUD operations on movie objects "
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return the current user's bookings
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer): 
        seat = serializer.validated_data['seat']
        seat.is_booked = True
        seat.save()
        serializer.save(user=self.request.user)
"Done 2/28/26, defines three views that handle displaying all movies, allowing logged-in users to book an available seat for a specific movie, and showing a logged-in user's booking history "

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

@login_required
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(is_booked=False)
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id)
        Booking.objects.create(movie=movie, seat=seat, user=request.user)
        seat.is_booked = True
        seat.save()
        return redirect('booking_history')
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
