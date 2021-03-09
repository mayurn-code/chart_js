from django.db import models


class Tag(models.Model):
    date_time = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField(max_length=100)
    humidity = models.FloatField(max_length=100)

    