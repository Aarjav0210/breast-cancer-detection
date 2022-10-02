#!/usr/bin/env python
# coding: utf-8

# In[76]:


from sklearn import datasets
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from collections import Counter


# In[ ]:


X_test1=pd.read_csv(r"")


# In[77]:


breast_cancer=datasets.load_breast_cancer()


# In[79]:


x=breast_cancer.data
y=breast_cancer.target
df=pd.DataFrame(x)


# In[80]:


df.columns=breast_cancer.feature_names
print(df.columns)


# In[100]:


df.head(5)


# In[101]:


df.iloc[20]


# In[126]:


ab=df.iloc[:,0:30].mean()
ab


# In[114]:


X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2)
df.describe()


# In[84]:


clf=KNeighborsClassifier(n_neighbors=9)
alg=clf.fit(X_train,Y_train)


# In[85]:


for i in range(1,16,2):
    clf=KNeighborsClassifier(n_neighbors=i)
    score=cross_val_score(clf,X_train,Y_train)
    print(i,score.mean())
    


# In[86]:


y_pred=alg.predict(X_test)


# In[87]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_test,y_pred)


# In[88]:


k=9
def predictone(X_train,Y_train,X_test,k):
    distances=[]
    for i in range(len(X_train)):
        distance=((X_train[i,:]-X_test)**2).sum()
        distances.append([distance,i])
    distances = sorted(distances)
    targets=[]
    for i in range(k):
        index_of_training_data=distances[i][1]
        targets.append(Y_train[index_of_training_data])
    return counter(targets).most_common(1)[0][0]    


# In[89]:


Y_predone=alg.predict(X_test)


# In[90]:


print(y_pred)


# In[91]:


Y_test


# In[92]:


df1 = pd.DataFrame(y_pred)


# In[93]:


df1.to_csv('output.csv')


# In[ ]:




