def insertSort(list):
    ls = len(list)
    for i in range(1, ls):
        for j in range(i):
            if list[i] <= list[j]:
                key = list.pop(i)
                list.insert(j, key)
                break
    return list
print(insertSort([5,3,8,2,0,1,8]))