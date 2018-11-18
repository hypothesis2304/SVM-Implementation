import numpy as np

def manage_data(X, Y):

    class1 = []
    class0 = []

    for i in range(len(Y)):
    	if Y[i] == 1:
    		class1.append(i)
    	else:
    		class0.append(i)
    trX1 = X[:, class1[:200]]
    trX0 = X[:, class0[:200]]

    trX = np.concatenate((trX1, trX0), axis=1)
    trY = np.concatenate((Y[class1[:200]], Y[class0[:200]]))

    valX1 = X[:,class1[200:250]]
    valX0 = X[:,class0[200:250]]

    valX = np.concatenate((valX1, valX0), axis=1)
    valY = np.concatenate((Y[class1[200:250]], Y[class0[200:250]]))

    tsX1 = X[:, class1[250:350]]
    tsX0 = X[:, class0[250:350]]

    tsX = np.concatenate((tsX1, tsX0), axis=1)
    tsY = np.concatenate((Y[class1[250:350]], Y[class0[250:350]]))

    return trX, trY, valX, valY, tsX, tsY
