from django.db import models


class Tour(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    announcement = models.TextField()
    date = models.DateField()
    event_program = models.TextField()
    thumbnail = models.ImageField(
        blank=True,
        upload_to="tours/thumbnails/",
    )

    def __str__(self):
        return self.title
