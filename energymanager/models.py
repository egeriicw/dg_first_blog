from __future__ import unicode_literals
from django.db import models

from datetime import datetime

# Create your models here.

class GSODWeatherData(models.Model):

    # FIELD   POSITION  TYPE   DESCRIPTION
    #
    # STN---  1-6       Int.   Station number (WMO/DATSAV3 number)
    #                          for the location.
    #
    # WBAN    8-12      Int.   WBAN number where applicable--this is the
    #                          historical "Weather Bureau Air Force Navy"
    #                          number - with WBAN being the acronym.
    #
    # YEAR    15-18     Int.   The year.
    #
    # MODA    19-22     Int.   The month and day.
    #
    # TEMP    25-30     Real   Mean temperature for the day in degrees
    #                          Fahrenheit to tenths.  Missing = 9999.9
    #
    #
    # Count   32-33     Int.   Number of observations used in
    #                          calculating mean temperature.
    #
    # DEWP    36-41     Real   Mean dew point for the day in degrees
    #                          Fahrenheit to tenths.  Missing = 9999.9
    #
    # Count   43-44     Int.   Number of observations used in
    #                          calculating mean dew point.
    #
    # SLP     47-52     Real   Mean sea level pressure for the day
    #                          in millibars to tenths.  Missing =
    #                          9999.9
    # Count   54-55     Int.   Number of observations used in
    #                          calculating mean sea level pressure.
    #
    # STP     58-63     Real   Mean station pressure for the day
    #                          in millibars to tenths.  Missing =
    #                          9999.9
    # Count   65-66     Int.   Number of observations used in
    #                          calculating mean station pressure.
    #
    # VISIB   69-73     Real   Mean visibility for the day in miles
    #                          to tenths.  Missing = 999.9
    #
    # Count   75-76     Int.   Number of observations used in
    #                          calculating mean visibility.
    #
    # WDSP    79-83     Real   Mean wind speed for the day in knots
    #                          to tenths.  Missing = 999.9
    #
    # Count   85-86     Int.   Number of observations used in
    #                          calculating mean wind speed.
    #
    # MXSPD   89-93     Real   Maximum sustained wind speed reported
    #                          for the day in knots to tenths.
    #                          Missing = 999.9
    #
    #
    # GUST    96-100    Real   Maximum wind gust reported for the day
    #                          in knots to tenths.  Missing = 999.9
    #
    #
    # MAX     103-108   Real   Maximum temperature reported during the
    #                          day in Fahrenheit to tenths--time of max
    #                          temp report varies by country and
    #                          region, so this will sometimes not be
    #                          the max for the calendar day.  Missing =
    #                          9999.9
    #
    # Flag    109-109   Char   Blank indicates max temp was taken from the
    #                          explicit max temp report and not from the
    #                          'hourly' data.  * indicates max temp was
    #                          derived from the hourly data (i.e., highest
    #                          hourly or synoptic-reported temperature).
    #
    # MIN     111-116   Real   Minimum temperature reported during the
    #                          day in Fahrenheit to tenths--time of min
    #                          temp report varies by country and
    #                          region, so this will sometimes not be
    #                          the min for the calendar day.  Missing =
    #                          9999.9
    #
    # Flag    117-117   Char   Blank indicates min temp was taken from the
    #                          explicit min temp report and not from the
    #                          'hourly' data.  * indicates min temp was
    #                          derived from the hourly data (i.e., lowest
    #                          hourly or synoptic-reported temperature).
    #
    # PRCP    119-123   Real   Total precipitation (rain and/or melted
    #                          snow) reported during the day in inches
    #                          and hundredths; will usually not end
    #                          with the midnight observation--i.e.,
    #                          may include latter part of previous day.
    #                          .00 indicates no measurable
    #                          precipitation (includes a trace).
    #                          Missing = 99.99
    #                          Note:  Many stations do not report '0' on
    #                          days with no precipitation--therefore,
    #                          '99.99' will often appear on these days.
    #                          Also, for example, a station may only
    #                          report a 6-hour amount for the period
    #                          during which rain fell.
    #                          See Flag field for source of data.
    # Flag    124-124   Char   A = 1 report of 6-hour precipitation
    #                              amount.
    #                          B = Summation of 2 reports of 6-hour
    #                              precipitation amount.
    #                          C = Summation of 3 reports of 6-hour
    #                              precipitation amount.
    #                          D = Summation of 4 reports of 6-hour
    #                              precipitation amount.
    #                          E = 1 report of 12-hour precipitation
    #                              amount.
    #                          F = Summation of 2 reports of 12-hour
    #                              precipitation amount.
    #                          G = 1 report of 24-hour precipitation
    #                              amount.
    #                          H = Station reported '0' as the amount
    #                              for the day (eg, from 6-hour reports),
    #                              but also reported at least one
    #                              occurrence of precipitation in hourly
    #                              observations--this could indicate a
    #                              trace occurred, but should be considered
    #                              as incomplete data for the day.
    #                          I = Station did not report any precip data
    #                              for the day and did not report any
    #                              occurrences of precipitation in its hourly
    #                              observations--it's still possible that
    #                              precip occurred but was not reported.
    #
    # SNDP    126-130   Real   Snow depth in inches to tenths--last
    #                          report for the day if reported more than
    #                          once.  Missing = 999.9
    #                         Note:  Most stations do not report '0' on
    #                          days with no snow on the ground--therefore,
    #                          '999.9' will often appear on these days.
    #
    # FRSHTT  133-138   Int.   Indicators (1 = yes, 0 = no/not
    #                          reported) for the occurrence during the
    #                          day of:
    #                          Fog ('F' - 1st digit).
    #                          Rain or Drizzle ('R' - 2nd digit).
    #                          Snow or Ice Pellets ('S' - 3rd digit).
    #                          Hail ('H' - 4th digit).
    #                          Thunder ('T' - 5th digit).
    #                          Tornado or Funnel Cloud ('T' - 6th
    #                          digit).

    station_text = models.CharField(max_length=6, blank=True)
    date_text = models.CharField(max_length=6, blank=True)
    date = models.DateField(blank=True)
    avg_oa_temp = models.FloatField(blank=True)
    dewpt = models.FloatField(blank=True)
    slp = models.FloatField(blank=True)
    stp = models.FloatField(blank=True)
    visib = models.FloatField(blank=True)
    wdsp = models.FloatField(blank=True)
    mxspd = models.FloatField(blank=True)
    gust = models.FloatField(blank=True)
    max_oa_temp = models.FloatField(blank=True)
    min_oa_temp = models.FloatField(blank=True)
    prcp = models.FloatField(blank=True)
    prcp_flag = models.CharField(max_length=1, blank=True)
    sndp = models.FloatField(blank=True)
    frshtt = models.IntegerField(blank=True)

class GSODWeatherStation(models.Model):

    # Integrated Surface Database Station History, April 2017
    #
    #  USAF = Air Force station ID. May contain a letter in the first position.
    #  WBAN = NCDC WBAN number
    #  CTRY = FIPS country ID
    #    ST = State for US stations
    #  ICAO = ICAO ID
    #   LAT = Latitude in thousandths of decimal degrees
    #   LON = Longitude in thousandths of decimal degrees
    #  ELEV = Elevation in meters
    # BEGIN = Beginning Period Of Record (YYYYMMDD). There may be reporting gaps within the P.O.R.
    #   END = Ending Period Of Record (YYYYMMDD). There may be reporting gaps within the P.O.R.

    usaf_id = models.CharField(max_length=6)
    wban_id = models.CharField(max_length=5)
    station_name = models.CharField(max_length=57)
    country_id = models.CharField(max_length=2)
    state_abv = models.CharField(max_length=2)
    icao_id = models.CharField(max_length=5)
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
    elev = models.CharField(max_length=10)
    date_begin = models.DateField(blank=False)
    date_end = models.DateField(blank=False)
    slug = models.SlugField(max_length=12, blank=True, null=True)

    data = models.ForeignKey(GSODWeatherData, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "{}-{}".format(self.usaf_id, self.wban_id)

class Address(models.Model):
    street_num = models.CharField(max_length=10)
    street_name1 = models.CharField(max_length=255)
    street_name2 = models.CharField(max_length=255, blank=True)
    street_name3 = models.CharField(max_length=255, blank=True)
    city_name = models.CharField(max_length=255, blank=True)
    state_name = models.CharField(max_length=20, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return "{} {} {} {}".format(self.street_num, self.street_name1, self.street_name2, self.street_name3)

class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True)

    # To add
    # type = models.OneToOneField(PlaceType)
    # classification = models.ForeignKey(PlaceClassification)
    # group = models.ForeignKey(PlaceGroup)
    # organization = models.ForeignKey(Organization)

    weather_station = models.OneToOneField(GSODWeatherStation, on_delete=models.CASCADE, blank=True, null=True)

    date_begin = models.DateField(default=datetime.strptime("1900-01-01", "%Y-%m-%d"), blank=False, null=True)
    date_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
