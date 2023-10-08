import pandas as pd
import numpy as np

df = pd.read_csv("../data/Iris.csv")
df.drop("Id", axis=1, inplace=True)

X = df.drop("Species", axis=1)
y = df["Species"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

import pickle
pickle.dump(model, open("model.pkl", "wb"))