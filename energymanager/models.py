from __future__ import unicode_literals
from django.db import models

from datetime import datetime

# Create your models here.

class Address(models.Model):
    street_num = models.TextField(max_length=10)
    street_name1 = models.TextField(max_length=255)
    street_name2 = models.TextField(max_length=255, blank=True)
    street_name3 = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return "{} {} {} {}".format(self.street_num, self.street_name1, self.street_name2, self.street_name3)

class Place(models.Model):
    name = models.TextField(max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True)

    # To add
    # type = models.OneToOneField(PlaceType)
    # classification = models.ForeignKey(PlaceClassification)
    # group = models.ForeignKey(PlaceGroup)
    # organization = models.ForeignKey(Organization)

    date_begin = models.DateField(default=datetime.strptime("1900-01-01", "%Y-%m-%d"), blank=False, null=True)
    date_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
