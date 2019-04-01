array = [1,2,3,10,4,78,1,23,1]
print(1.2 - 1.0 == 0.2)
print ('a' < 'b')
def bubble_sort(arr):
    n = len(arr)  #8
    for i in range(0, n):
        for j in range(0, n - i - 1):   #6
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+ 1] = arr[j + 1],arr[j]

bubble_sort(array)
print(array)