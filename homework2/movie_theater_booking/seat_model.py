"Caroline Duncan, 2/27/26, each seat has a number and whether it's booked or not "
class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat_number}"â
