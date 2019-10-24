
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


data.head()

__________________________________________________________________________________________________________________

# Candidate-Elimination using csv-library

import csv

s=[0,0,0,0,0,0]
g=["?","?","?","?","?","?"]
p=["?","?","?","?","?","?"]

def gen():
	for k in range(1,len(i)-1):
		if i[k]!=s[k-1]:
			g[k-1]=s[k-1]


with open("/home/monisha/machine-learning-lab-vtu/datasets/enjoysport.csv") as csvfile:
	csvreader=csv.reader(csvfile)
	for i in csvreader:
		if i[6]=="yes":
			if s[0] == 0:
				s=i[:6]
			else:
				for k in range(0,len(i)-1):
					if i[k] != s[k-1]:
						s[k-1]="?"
		else:
			gen()
	gen()

print("specific hypothesis:",s)
print("general hypothesis")
for i ine range(0,leng(g)):
	if g[i] !="?":
		p[i]=g[i]
		print(p)
	p[i]="?"

























