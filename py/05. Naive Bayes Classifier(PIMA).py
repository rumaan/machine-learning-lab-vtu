
# coding: utf-8

# In[1]:


import csv
import random
import numpy as np
import pandas as pd
import math


# In[2]:


def mean(numbers):
    return sum(numbers) / float(len(numbers) - 1)


# In[3]:


def stddev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)


# In[4]:


data = []


# In[5]:


lines = csv.reader(open('datasets/pima-indians.csv', 'r'))


# In[6]:


data = list(lines)


# In[7]:


for i in range(len(data)):
    data[i] = [float(x) for x in data[i]]


# In[8]:


trainset = []


# In[9]:


test = list(data)


# In[10]:


while len(trainset) < 564:
    index = random.randrange(len(test))
    trainset.append(test.pop(index))


# In[11]:


seperated = {}


# In[12]:


for i in range(564):
    vector = data[i]
    if vector[-1] not in seperated:
        seperated[vector[-1]] = []
    seperated[vector[-1]].append(vector[0:-1])


# In[13]:


summaries = {}


# In[14]:


for classvalue, instances in seperated.items():
    for attribute in zip(*instances):
        summaries[classvalue] =[(mean(attribute), stddev(attribute)) for attribute in zip(*instances)]


# In[15]:


prediction = []


# In[16]:


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


# In[17]:


correct = 0


# In[18]:


for i in range(204):
    print(test[i][-1], " ", prediction[i][-1])
    if test[i][-1] == prediction[i][-1]:
        correct += 1


# In[19]:


print(correct)


# In[20]:


print('Accuracy: {0}'.format((correct / 204.0) * 100))

