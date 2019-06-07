import pandas as pd
import numpy as np

def read_data():
    # import data
    Dataset = pd.read_csv('Titanic.csv')

    # select 'pclass', 'sex', 'age', 'sibsp' and set 'survived' as dependent variable
    df = pd.DataFrame(Dataset[['pclass','sex','age','sibsp','survived']])
    df = df.dropna()
    dataset_train = df.sample(frac=0.7)  # select 70% as train dataset
    rowlist = []
    for index in dataset_train.index:
        rowlist.append(index)
    dataset_test = df.drop(rowlist, axis=0)
    print(dataset_test)
    return dataset_train, dataset_test

#Scaling the data
def DataScaling(a):
    xmat = []
    ymat = []
    if a[0] == '1st':
        a[0] = 0.1
    elif a[0] == '2nd':
        a[0] = 0.2
    else:
        a[0] = 0.3

    if a[1] == 'female':
        a[1] = 0
    else:
        a[1] = 1
    # a[2] = a[2] / 100
    xmat.append(a[0])
    xmat.append(a[1])
    xmat.append(a[2])
    xmat.append(a[3])
    ymat.append(a[4])
    return xmat,ymat

# transfer dataset into matrix
def Datamat(df):
    Xmat = []
    Ymat = []
    for i in range(len(df) -1):
        xmat,ymat = DataScaling(df.values[i])
        Xmat.append(xmat)
        Ymat.append(ymat)
    Xmat = np.mat(Xmat)
    Ymat = np.mat(Ymat)
    return Xmat, Ymat

#Sigmoid Function
def sigmoid(data):
    return 1 / (1 + np.exp(-data))

# W,b
def SGD(X,ymat,alpha = 0.4, MaxIter = 10000,n_hidden_dim = 2, reg_lambda = 0):
    # alpha: steps
    # n_hidden_dim: hidden layer
    #FP
    W1 = np.mat(np.random.randn(4, n_hidden_dim))
    b1 = np.mat(np.random.randn(1, n_hidden_dim))
    W2 = np.mat(np.random.randn(n_hidden_dim,1))
    b2 = np.mat(np.random.randn(1, 1))

    for stepi in range(MaxIter):
        z1 = X * W1 + b1    #(731,4)*(4,2) + (731,2) = (731,2)
        a1 = sigmoid(z1)    #(731,2)
        z2 = a1 * W2 + b2   #(731,2)*(2,1) + (731,1) = (731,1)
        a2 = sigmoid(z2)    #(731,1)

        #BP
        a0 = X.copy()
        delta2 = a2 - ymat  #(731,1)
        delta1 = np.mat((delta2 * W2.T).A * (a1.A * (1-a1).A))
                        #(731,1)* (1,2) * (731,2) = (731, 2)
        dw1 = a0.T*delta1 + reg_lambda * W1 #(4, 731) * (731,2) + (4,2) = (4,2)
        db1 = np.sum(delta1,0)
        dw2 = a1.T*delta2 + reg_lambda * W2
        db2 = np.sum(delta2,0)

        W1 -= alpha * dw1
        b1 -= alpha * db1
        W2 -= alpha * dw2
        b2 -= alpha * db2

    print('w1:',W1)
    print('b1:',b1)
    print('w2:',W2)
    print('b2:',b2)
    return W1,b1,W2,b1

def buildmodel(x, W1,b1,W2,b2):
    # input_x: (1,4)
    a = x * W1 + b1
    b = a * W2
    b_1 = np.array(b)
    b_2 = np.array(b2)
    b = b_1[0][0] + b_2[0][0]
    b = sigmoid(b)
    return b

def predict(df):
    result = []
    for i in range(len(train_xmat) - 1):
        value = buildmodel(train_xmat[i], W1, b1, W2, b2)
        result.append(value)
    return result
def compare(df1, df2):
    Count_sur = 0
    Count_fat = 0
    Correct_sur = 0
    Correct_fat = 0
    for i in range(len(df1) -1 ):
        if df1[i] == df2[i] and df1[i] == 1:
            Correct_sur += 1
        if df1[i] == df2[i] and df1[i] == 0:
            Correct_fat += 1
        if df1[i] == 0:
            Count_fat += 1
        Count_sur = len(df1) - Count_fat
    return Correct_sur/Count_sur, Correct_fat/ Count_fat




dataset_train, dataset_test = read_data()
train_xmat, train_ymat = Datamat(dataset_train)
test_xmat, test_ymat = Datamat(dataset_test)
print(train_ymat.shape)
W1,b1,W2,b2 = SGD(train_xmat, train_ymat)

# step 3, compare:
train_result = predict(train_xmat)
test_result = predict(test_xmat)
train_sur, train_fat = compare(train_ymat, train_result)
test_sur, test_fat = compare(test_ymat, test_result)

print('in‐sample percent survivors correctly predicted (on training set) is',train_sur)
print('in-sample percent fatalities correctly predicted (on training set) is ', train_fat)
print('out‐sample percent survivors correctly predicted (on training set) is', test_sur)
print('out-sample percent fatalities correctly predicted (on training set) is ', test_fat)


