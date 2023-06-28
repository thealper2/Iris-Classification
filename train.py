import pandas as pd
import numpy as np

df = pd.read_csv("data/iris.csv")
X = df.drop("species", axis=1)
y = df["species"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

import pickle
pickle.dump(model, open("models/model.pkl", "wb"))
