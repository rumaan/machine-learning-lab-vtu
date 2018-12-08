# coding: utf-8
import csv
import random
import numpy as np
import pandas as pd
import math
def mean(numbers):
    return sum(numbers) / float(len(numbers) - 1)
def stddev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)
data = []
lines = csv.reader(open('datasets/pima-indians.csv', 'r'))
data = list(lines)
for i in range(len(data)):
    data[i] = [float(x) for x in data[i]]
trainset = []
test = list(data)
while len(trainset) < 564:
    index = random.randrange(len(test))
    trainset.append(test.pop(index))
seperated = {}
for i in range(564):
    vector = data[i]
    if vector[-1] not in seperated:
        seperated[vector[-1]] = []
    seperated[vector[-1]].append(vector[0:-1])
summaries = {}
for classvalue, instances in seperated.items():
    for attribute in zip(*instances):
        summaries[classvalue] =[(mean(attribute), stddev(attribute)) for attribute in zip(*instances)]
prediction = []
for i in range(204):
    probabilities = {}
    vector = test[i]
    for classvalue, classummary in summaries.items():
        probabilities[classvalue] = 1
        for j in range(len(classummary)):
            smean, sstdev = classummary[j]
            x = vector[j]
            expo = math.exp(-(math.pow(x - smean, 2)/(2 * math.pow(sstdev, 2))))
            probabilities[classvalue] *= (1 / (math.sqrt(2 * math.pi) * sstdev)) * expo
        bestlabel, bestprob = None, -1
        for classvalue, probability in probabilities.items():
            if bestlabel is None or probability > bestprob:
                bestprob = probability
                bestlabel = classvalue
        result = bestprob, bestlabel
        prediction.append(result)
correct = 0
for i in range(204):
    print(test[i][-1], " ", prediction[i][-1])
    if test[i][-1] == prediction[i][-1]:
        correct += 1
print(correct)
print('Accuracy: {0}'.format((correct / 204.0) * 100))
