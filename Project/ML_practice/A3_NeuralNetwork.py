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
    dataset_test = Dataset.drop(rowlist, axis=0)
    return dataset_train, dataset_test

#Scaling the data
def DataScaling(a):
    xmat = []
    ymat = []
    if a[0] == '1st':
        a[0] = 1
    elif a[0] == '2nd':
        a[0] = 2
    else:
        a[0] = 3

    if a[1] == 'female':
        a[1] = 0
    else:
        a[1] = 1
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

dataset_train, dataset_test = read_data()
train_xmat, train_ymat = Datamat(dataset_train)
test_xmat, test_ymat = Datamat(dataset_test)
print(test_xmat.shape)