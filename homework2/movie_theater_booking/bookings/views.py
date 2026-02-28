"Caroline Duncan, 2/28/26, sets up a rest api endpoint that lets authenticated-or-open users perform full CRUD operations on movie objects "
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

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
