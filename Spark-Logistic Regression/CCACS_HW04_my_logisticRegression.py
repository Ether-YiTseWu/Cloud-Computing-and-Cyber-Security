import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import time
import random
import requests

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def myTrain(iteration, lr, set_ratio):
    start = time.time()
    ### Proprecessing
    # Setup Variable
    dataset = []
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
    r = requests.get(url)
    open('dataset.txt', 'wb').write(r.content)
    f = open('.\\dataset.txt')

    # Make Dataset
    for line in f:
        oneLineData = []
        arr = line.strip()
        arr = line.split(",")
        for element in arr:
            oneLineData.append(float(element))
        dataset.append(oneLineData)

    ### Training
    # Ser up variables
    weight = []
    for i in range(4):
        weight.append(random.uniform(0, 1))
    bias = random.uniform(0, 1)
    loss = 0
    loss_history = []
    datasetOrder = list(range(len(dataset)))
    trainIndex = round(len(dataset)*set_ratio)
    testIndex  = round(len(dataset))
    random.shuffle(datasetOrder)            # Make the dataset order random
    
    # Iteration
    while (True):
        # Set break condition and Reset
        iteration -= 1
        if iteration < 0 :
            break
        predict = 0
        loss = 0
        weightChange = [0, 0, 0, 0]
        biasChange = 0

        # Train
        dataset = np.array(dataset)        # Tranform list to nparray for computation
        weight  = np.array(weight)
        for i in datasetOrder[0:trainIndex]:
            data = dataset[i]
            ax = sum(data[0:4]*weight)
            predict = sigmoid(ax + bias)
            loss = -(data[4]*math.log(predict) + (1-data[4])*math.log(1-predict)) + loss
            biasChange    = biasChange + (predict - data[4])
            for i in range(4):
                weightChange[i] = weightChange[i]  + (predict - data[4])*data[i]
        # Renew the parameters
        weight = weight - lr/len(dataset) * np.array(weightChange)
        bias   = bias   - lr/len(dataset) * biasChange
        loss_history.append(loss/trainIndex)
    end   = time.time()
    print("\nMy logistic regression algorithm spends " + str(end-start) + " s\n")
    # Get and print the result
    correct = 0
    for i in datasetOrder[trainIndex:testIndex]:
        data = dataset[i]
        ax = sum(data[0:4]*weight)
        predict = sigmoid(ax + bias)
        if data[4] == round(predict):
            correct += 1
    print("Training Dataset Length : " + str(trainIndex))
    print("Testing  Dataset Length : " + str(testIndex-trainIndex))
    print("Weights is : " + str(weight))
    print("Bias    is : " + str(bias) + "\n")
    print("Error     : " + str(loss/trainIndex))
    print("Accuracy : " + str(correct/(testIndex-trainIndex)))
    
    # Plot
    plt.plot(loss_history)
    plt.title('Train Error')
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.show()

# myTrain(iteration, lr, set_ratio):
myTrain(200, 0.1, 0.65)