#Import Needed Library
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

#Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

#Split Iris Dataset 80:20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

#Build Model
mdl = RandomForestClassifier(n_estimators=10)

#Train Model
mdl.fit(X_train, y_train)

#Predict Model
pred = mdl.predict(X_test)

print(accuracy_score(pred, y_test))

import pickle as pk
with open("rf.pkl", "wb") as dump_model:
    pk.dump(mdl, dump_model)