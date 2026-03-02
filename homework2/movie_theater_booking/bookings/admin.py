"Caroline Duncan, 3/1/26,registers the movie,seat and booking models with the admin site, making them manageable through the  admin interface.  "
from django.contrib import admin
from .models import Movie, Seat, Booking

admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Booking)
# Register your models here.
