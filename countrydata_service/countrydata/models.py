from django.db import models

class CountryData(models.Model):
    country_code = models.CharField(max_length=3, unique=True)
    population = models.IntegerField()
    capital = models.CharField(max_length=100)

    def __str__(self):
        return self.country_code
