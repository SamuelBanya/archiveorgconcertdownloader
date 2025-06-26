from django.db import models
import datetime

from django.db import models
from django.utils import timezone

# Band
class Band(models.Model):
    band_name = models.CharField(max_length=200)
    def __str__(self):
        return self.band_name

# Concert
class Concert(models.Model):
    internet_archive_identifier = models.CharField(max_length=200)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    publication_date = models.DateTimeField("date concert was held")
    flac_present = models.BooleanField(default=False)
    def __str__(self):
        return self.internet_archive_identifier
