
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


data = pd.read_csv('datasets/enjoysport.csv')


# In[ ]:


concepts = np.array(data.iloc[:, 0:-1])
target = np.array(data.iloc[:, -1])


# In[ ]:


def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for i in range(len(specific_h))] for j in range(len(specific_h))]
    for i, h in enumerate(concepts):
        if target[i] == 'yes':
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == 'no':
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    return specific_h, general_h


# In[ ]:


s_final, g_final = learn(concepts, target)


# In[ ]:


print('Final S: ', s_final, sep="\n")
print('Final G: ', g_final, sep="\n")


# In[ ]:


data.head()

