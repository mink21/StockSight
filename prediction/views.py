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

def Display(request, companyID, optionsID):
    company = get_object_or_404(Company, pk = companyID)
    options = get_object_or_404(Options, pk = optionsID)
    trainStart = options.startDate
    trainEnd = options.endDate
    start = options.startDate
    end = options.endDate
    tickerSymbol = company.tickerSymbol
    companyName = company.companyName
    predict = options.predict
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

def pickCompany(request):
    companyList = Company.objects.order_by("companyName")[:5]
    #lastest_question_list.reverse()
    context = {
        'companyList':companyList
    }
    return render(request, "prediction/companyPicker.html", context)

def pickOptions(request, companyID):
    optionsList = Options.objects.order_by("endDate")[:5]
    #lastest_question_list.reverse()
    context = {
        'optionsList':optionsList,
        'companyID':companyID
    }
    return render(request, "prediction/optionPicker.html", context)