from sklearn import linear_model
import numpy as np
m,n = map(int, input().split())
X = []
Y = []

for i in range(n):
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])

q = int(input().strip())
X_new = []
for i in range(q):
    X_new.append(input().strip().split(' '))
X = np.array(X,float)
Y = np.array(Y,float)
X_new = np.array(X_new,float)   
lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_
#print a, b[0], b[1]
result = lm.predict(X_new)
for i in range(len(result)):
    print(round(float(result[i]),2))
