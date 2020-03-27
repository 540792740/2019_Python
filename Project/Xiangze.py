import pandas as pd

data = pd.read_excel('test.xlsx')
list1 = data.values.tolist()
# 105 114
ls = len(list1)
Positive = []
for i in range(ls):
    print(list1[i][105])
    if list1[i][105] == 1:
        print(list1[i][0])
        Positive.append(list1[i][0])
print(Positive)
