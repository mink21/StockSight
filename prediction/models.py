from django.db import models
import datetime as dt


class Company(models.Model):
    tickerSymbol = models.CharField(max_length=5)
    companyName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.companyName

class Options(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    startDate = models.DateTimeField(default=dt.datetime(2021,1,1))
    endDate = models.DateTimeField(default=dt.datetime.now())
    trainStartDate = models.DateTimeField(default=dt.datetime(2020,1,1))
    trainEndDate = models.DateTimeField(default=dt.datetime(2021,1,1))
    predict = models.BooleanField(default=True)
    predictionDays = models.IntegerField(default=60)

    def __str__(self):
        if self.predict:
            return f'{self.company.companyName} stocks predicted alongside real values'
        return f'{self.company.companyName} stocks displayed'