'''

'''
def bubble_sort(arr):
    ls = len(arr)  #8
    for i in range(0, ls):
        for j in range(0, ls - i - 1):   #6
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+ 1] = arr[j + 1],arr[j]

array = [1,2,3,10,4,78,1,23,1]
bubble_sort(array)
print(array)

print(1.2 - 1.0 == 0.2)
print ('a' < 'b')
