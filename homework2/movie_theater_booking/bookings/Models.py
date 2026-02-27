"Caroline Duncan, 2/26/26, Class to store movies where they can be stored."
class Movie(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text = "Time in minutes")

    def__str__(self):
       return self.title
