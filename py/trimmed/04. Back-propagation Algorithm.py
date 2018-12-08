# coding: utf-8
import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X, axis=0)
y = y / 100
def sigmoid(x):
    return 1/(1 + np.exp(-x))
def derivatives_sigmoid(x):
    return x * (1 - x)
epoch = 7000
learning_rate = 0.1
inputlayer_neurons = 2
hiddenlayer_neurons = 3
outputlayer_neurons = 1
# Weight of hidden layer
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
# Bias of hidden layer
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
# Weight of output layer
wo = np.random.uniform(size=(hiddenlayer_neurons, outputlayer_neurons))
# Bias of output layer
bo = np.random.uniform(size=(1, outputlayer_neurons))
# training
for i in range(epoch):
    # Sum of (input * weights in hidden layer) + bias of hidden
    net_h = np.dot(X, wh) + bh
    # Apply Activation Function
    sigma_h = sigmoid(net_h)
    net_o = np.dot(sigma_h, wo) + bo
    # Apply Activation Function
    output = sigmoid(net_o)
    
    # Finding Deltas (Cost Function Implementation)
    # Delta of O/P layer
    deltaK = (y - output) * derivatives_sigmoid(output)
    # Delta of Hidden Layer
    deltaH = deltaK.dot(wo.T) * derivatives_sigmoid(sigma_h)
    # Update the weights
    wo = wo + sigma_h.T.dot(deltaK) * learning_rate
    wh = wh + X.T.dot(deltaH) * learning_rate
    
    error = sum(deltaK)**2 / len(deltaK)
    
    print('Epoch -> {0}, lrate -> {1}, error -> {2}'.format(i, learning_rate, error))
print("Input: \n " + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n", output)
