from django.http import HttpResponse
import stockPredictRefactored as predictor
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Company, Options, Source
import matplotlib.pyplot as plt
import datetime as dt

def index(request):
    return HttpResponse("Hello, world. You're at the prediction index.")

def Display(request, companyID, optionsID, sourceID):
    company = get_object_or_404(Company, pk = companyID)
    source = get_object_or_404(Source, pk = sourceID)
    options = get_object_or_404(Options, pk = optionsID)
    trainStart = options.startDate
    trainEnd = options.endDate
    start = options.startDate
    end = options.endDate
    tickerSymbol = company.tickerSymbol
    source = source.source
    predict = options.predict
    DisplayBackend(trainStart, trainEnd, start, end, tickerSymbol, source, predict)

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

def pickSource(request):
    sourceList = Source.objects.order_by("source")[:5]
    context = {
        'sourceList':sourceList
    }
    return render(request, "prediction/sourcePicker.html", context)

def pickCompany(request, sourceID):
    companyList = Company.objects.order_by("tickerSymbol")[:5]
    #lastest_question_list.reverse()
    context = {
        'companyList':companyList,
        'sourceID':sourceID
    }
    return render(request, "prediction/companyPicker.html", context)

def pickOptions(request, companyID, sourceID):
    optionsList = Options.objects.order_by("endDate")[:5]
    #lastest_question_list.reverse()
    context = {
        'optionsList':optionsList,
        'sourceID':sourceID,
        'companyID':companyID
    }
    return render(request, "prediction/optionPicker.html", context)