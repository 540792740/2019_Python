import numpy as np

'''
Author: Jiawei Wang
CWID: 10431455
Email:peterwangjiawei@gmail.com
Content: Assignment1.2 Gradient descent way to solve Linear Regressipon
        I set the data set from 100 to 1000 to make result more accurate
'''

def G_decent(x1,x2,x3, Y, times, alpha, lam):
    X = np.mat(np.zeros((100,3)))
    m,n = X.shape
    # 1000 * 3 matrix, linear model prediction
    X[:,0] = x1
    X[:,1] = x2
    X[:,2] = x3

    W = np.mat(np.random.randn(3,1))
    b = np.mat(np.random.randn(1,1))
    i = 0
    # iterations
    while i < times:
        H = X * W + b
        dw = (1 / m) * X.T * (H - Y) + (1 / m) * lam * W
        db = (1 / m) * np.sum(H - Y)    #matrix(1,1)
        i += 1
        W -= alpha * dw
        b -= alpha * db
    return W,b

#data set, x1,x2,x3 are 1000*1 matrix
x1 = 2 * np.random.rand(100, 1)
x2 = 2 * np.random.rand(100, 1)
x3 = 2 * np.random.rand(100, 1)
y = 3 * x1 + 4 * x2 + 5 * x3 + np.random.randn(100, 1) + 2

w1,b = G_decent(x1,x2,x3,y,100000,0.001,2)
# x1,x2,x3,y are input data
# 10000 is max iteration times
# 0.1 is alpha, length of step
# 2 is lambada,
print('w1 : ', w1[0,0])
print('w2 : ', w1[1,0])
print('w3 : ', w1[2,0])
print('b  : ', b [0,0])
