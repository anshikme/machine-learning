import numpy as np
import matplotlib.pyplot as plt

data = open("C:\\Users\\science\\Downloads\\data_1d.csv")
X=[]
Y=[]
for i in data:
    x,y= i.split(",")
    X.append(float(x))
    Y.append(float(y))

    
    
X = np.array(X)  
Y = np.array(Y)    

plt.scatter(X,Y)
plt.show()

#denominator =  ∑(X^2) - x̄*∑(X)
denominator = X.dot(X)- (X.mean()* X.sum())

a = ((Y.mean()*X.dot(X))- (X.mean()*X.dot(Y)))/denominator
b = (np.dot(X,Y) - np.sum(X)* np.mean(Y))/denominator

Yhat = []    
# y = bX +a 
Yhat= b*X + a

plt.scatter(X,Y)
plt.plot(X,Yhat)
plt.show()
