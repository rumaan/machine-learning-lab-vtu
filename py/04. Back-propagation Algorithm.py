
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)


# In[3]:


y = np.array(([92], [86], [89]), dtype=float)


# In[4]:


X = X/np.amax(X, axis=0)


# In[5]:


y = y / 100


# In[6]:


def sigmoid(x):
    return 1/(1 + np.exp(-x))


# In[7]:


def derivatives_sigmoid(x):
    return x * (1 - x)


# In[8]:


epoch = 7000


# In[9]:


learning_rate = 0.1


# In[10]:


inputlayer_neurons = 2


# In[11]:


hiddenlayer_neurons = 3


# In[12]:


outputlayer_neurons = 1


# In[13]:


# Weight of hidden layer
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))


# In[14]:


# Bias of hidden layer
bh = np.random.uniform(size=(1, hiddenlayer_neurons))


# In[15]:


# Weight of output layer
wo = np.random.uniform(size=(hiddenlayer_neurons, outputlayer_neurons))


# In[16]:


# Bias of output layer
bo = np.random.uniform(size=(1, outputlayer_neurons))


# In[17]:


# training
for i in range(epoch):
    # Sum of (input * weights in hidden layer) + bias of hidden
    net_h = np.dot(X, wh) + bh
    # Apply Activation Function
    sigma_h = sigmoid(net_h)
    # Input to O/P Layer = (O/P of Hidden Layer * weight of O/P Layer) + bias of O/P layer
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


# In[18]:


print("Input: \n " + str(X))


# In[19]:


print("Actual Output: \n" + str(y))


# In[20]:


print("Predicted Output: \n", output)

