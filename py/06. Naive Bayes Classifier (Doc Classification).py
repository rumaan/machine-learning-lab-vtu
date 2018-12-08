
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


msg = pd.read_csv('datasets/text_doc.csv', names=['message', 'label'])


# In[ ]:


print("Total Instances of Dataset: ", msg.shape[0])


# In[ ]:


msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})


# In[ ]:


X = msg.message


# In[ ]:


y = msg.labelnum


# In[ ]:


from sklearn.model_selection import train_test_split


# In[ ]:


Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)


# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer


# In[ ]:


count_v = CountVectorizer()


# In[ ]:


Xtrain_dm = count_v.fit_transform(Xtrain)


# In[ ]:


Xtest_dm = count_v.transform(Xtest)


# In[ ]:


df = pd.DataFrame(Xtrain_dm.toarray(),columns=count_v.get_feature_names())


# In[ ]:


print(df[0:5])


# In[ ]:


from sklearn.naive_bayes import MultinomialNB


# In[ ]:


clf = MultinomialNB()


# In[ ]:


clf.fit(Xtrain_dm, ytrain)


# In[ ]:


pred = clf.predict(Xtest_dm)


# In[ ]:


for doc, p in zip(Xtrain, pred):
    p = 'pos' if p == 1 else 'neg'
    print("%s -> %s" % (doc, p))


# In[ ]:


from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score


# In[ ]:


print('Accuracy Metrics: \n')
print('Accuracy: ', accuracy_score(ytest, pred))


# In[ ]:


print('Recall: ', recall_score(ytest, pred))


# In[ ]:


print('Precision: ', precision_score(ytest, pred))


# In[ ]:


print('Confusion Matrix: \n', confusion_matrix(ytest, pred))

