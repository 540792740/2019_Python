array = [2,4,2,14,77,24,2,14]

def QuickSort(arr):
    Sort(arr, 0, len(arr) - 1)

def Sort(arr, low, high):
    i = low
    j = high
    if low <= high:
        pivot = arr[i]
        while(i < j):
            while(i < j and arr[j] >= pivot):
                j -= 1
            arr[i] = arr[j]

            while(i < j and arr[i] <= pivot):
                i += 1
            arr[j] = arr[i]

        arr[i] = pivot
        Sort(arr, low, i - 1)
        Sort(arr, i + 1, high)

QuickSort(array)
print(array)