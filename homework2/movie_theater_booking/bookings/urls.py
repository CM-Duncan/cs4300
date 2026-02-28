"Caroline Duncan, 2/28,26, registers three viewsets with a DRF router, which automatically generates all the standard REST API URLs"
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = router.urls
