import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout, LSTM

scaler = MinMaxScaler(feature_range=(0,1))
prediction_days = 60

def LoadData(start, end, company, companyName):
    data = web.DataReader(company, companyName, start, end)
    return data

def PrepareData(data):
    
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))
    return scaled_data

def TrainModel(scaled_data):
    x_train = []
    y_train = []

    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x-prediction_days:x, 0])
        y_train.append(scaled_data[x,0])
        
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1],1))

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1],1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1)) #prediction of the next closing value
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=25, batch_size=32)
    return model

def Predict(trainStart, trainEnd, start, end, company, companyName):
    model = TrainModel(PrepareData(LoadData(start, end, company, companyName)))
    trainData = LoadData(trainStart, trainEnd, company, companyName)
    predictData = LoadData(start, end, company, companyName)

    total_dataset = pd.concat((trainData['Close'], predictData['Close']), axis=0)
    total_dataset = pd.concat((trainData['Close'], predictData[ 'Close']), axis=0)
    model_inputs = total_dataset[len(total_dataset) - len(predictData)-prediction_days:].values
    model_inputs = model_inputs.reshape(-1, 1)
    model_inputs = scaler.transform (model_inputs)

    x_test = []
    for x in range (prediction_days, len(model_inputs)):
        x_test.append (model_inputs [x-prediction_days:x, 0])

    x_test = np.array (x_test)
    x_test = np.reshape (x_test, (x_test.shape[0], x_test.shape[1], 1))
    predictedPrices = model.predict(x_test)
    predictedPrices = scaler.inverse_transform (predictedPrices)
    return predictedPrices

def getReal(start, end, company, companyName):
    data = LoadData(start, end, company, companyName)
    actualPrices = data['Close'].values
    return actualPrices

# def Display(trainStart, trainEnd, start, end, company, companyName, predict, real):
#     if not predict and not real:
#         return
#     predictedPrices = Predict(trainStart, trainEnd, start, end, company, companyName)
#     actualPrices = getReal(start, end, company, companyName)
#     if predict:
#         plt.plot(predictedPrices, color='green', label=f"Predicted {company} Price")
#     if real:
#         plt.plot(actualPrices, color="black", label=f"Actual {company} Price")
#     plt.title(f"{company} Share Price")
#     plt.xlabel('Time')
#     plt.ylabel(f'{company} Share Price')
#     plt.legend ()
#     plt.show()


# Display(dt.datetime(2020,1,1), dt.datetime(2021,1,1), dt.datetime(2021,1,1), dt.datetime.now(), "FB", "yahoo", True, True)