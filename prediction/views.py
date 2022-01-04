from django.http import HttpResponse
import stockPredictRefactored as predictor
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Company, Options
import matplotlib.pyplot as plt
import datetime as dt

def index(request):
    return HttpResponse("Hello, world. You're at the prediction index.")

#This is what I think the display function should look like after we pick the right options
# def Display(request, companyID, optionsID):
#     company = get_object_or_404(Company, pk = companyID)
#     options = get_object_or_404(Options, pk = optionsID)
#     trainStart = options.startDate
#     trainEnd = options.endDate
#     start = options.startDate
#     end = options.endDate
#     tickerSymbol = company.tickerSymbol
#     companyName = company.companyName
#     predict = options.predict

def Display(request):
    trainStart = dt.datetime(2020,1,1)
    trainEnd = dt.datetime(2021,1,1)
    start = dt.datetime(2021,1,1)
    end = dt.datetime(2022,1,1)
    tickerSymbol = "FB"
    companyName = "yahoo"
    predict = True
    DisplayBackend(trainStart, trainEnd, start, end, tickerSymbol, companyName, predict)

def DisplayBackend(trainStart, trainEnd, start, end, tickerSymbol, companyName, predict):
    if predict:
        predictedPrices = predictor.Predict(trainStart, trainEnd, start, end, tickerSymbol, companyName)
        actualPrices = predictor.getReal(start, end, tickerSymbol, companyName)
        plt.plot(predictedPrices, color='green', label=f"Predicted {tickerSymbol} Price")

    plt.plot(actualPrices, color="black", label=f"Actual {tickerSymbol} Price")
    plt.title(f"{tickerSymbol} Share Price")
    plt.xlabel('Time')
    plt.ylabel(f'{tickerSymbol} Share Price')
    plt.legend ()
    plt.show()
    