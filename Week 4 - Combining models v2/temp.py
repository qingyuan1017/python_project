# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydot_ng as pydot
#%matplotlib inline

from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from IPython.display import Image # displaying images files in jupyter
from IPython.display import IFrame # displaying pdf file in jupyter



heart = pd.read_csv('heart.csv')
del heart['Unnamed: 0']
heart=heart.dropna()

heart['AHD']=(heart['AHD']=='Yes').astype(np.int)
df_thal = pd.get_dummies(heart['Thal'],prefix='Thal')

heart = pd.concat([heart, df_thal], axis=1)
heart = pd.concat([heart, pd.get_dummies(heart['ChestPain'],prefix='ChestPain')], axis=1)

X_labels = [c for c in heart.columns if c not in ['AHD','Thal','ChestPain']]
X = heart.ix[:,X_labels]
Y = heart['AHD']


base_clf = tree.DecisionTreeClassifier(max_depth=3)
#clf = BaggingClassifier(n_estimators=10, base_estimator=base_clf, oob_score=True)
clf = BaggingClassifier(n_estimators=100, oob_score=True)
clf = clf.fit(X,Y)    
print(clf.oob_score_)