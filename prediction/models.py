from django.db import models
import datetime as dt


class Source(models.Model):
    source = models.CharField(max_length=100, default="yahoo")
    def __str__(self):
        return self.source


class Company(models.Model):
    tickerSymbol = models.CharField(max_length=5)
    companyName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tickerSymbol

class Options(models.Model):
    startDate = models.DateTimeField(default=dt.datetime(2021,1,1))
    endDate = models.DateTimeField(default=dt.datetime.now())
    trainStartDate = models.DateTimeField(default=dt.datetime(2020,1,1))
    trainEndDate = models.DateTimeField(default=dt.datetime(2021,1,1))
    predict = models.BooleanField(default=True)
    predictionDays = models.IntegerField(default=60)