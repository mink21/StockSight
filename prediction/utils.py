import matplotlib.pyplot as plt
import datetime as dt
import stockPredictRefactored as predictor
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format = "png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

# def get_plot(x,y):
    


def DisplayBackend(trainStart, trainEnd, start, end, tickerSymbol, companyName, predict):
    plt.switch_backend('AGG')
    if predict:
        predictedPrices = predictor.Predict(trainStart, trainEnd, start, end, tickerSymbol, companyName)
        actualPrices = predictor.getReal(start, end, tickerSymbol, companyName)
        plt.plot(predictedPrices, color='green', label=f"Predicted {tickerSymbol} Price")
    plt.plot(actualPrices, color="black", label=f"Actual {tickerSymbol} Price")
    plt.title(f"{tickerSymbol} Share Price")
    plt.xlabel('Time')
    plt.ylabel(f'{tickerSymbol} Share Price')
    plt.legend ()

    graph = get_graph()
    return graph
