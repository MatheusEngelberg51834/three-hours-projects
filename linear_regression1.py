from sklearn import linear_model
import numpy as np

X = [3, 5, 2.5, 6, 5.5, 7, 8, 8]
y = [1, 3, 4, 5, 6, 7, 7, 8,]

X = np.reshape(X, (-1, 1))

model = linear_model.LinearRegression()

model.fit(X, y)

X_new = [[10]]
print(model.predict(X_new))