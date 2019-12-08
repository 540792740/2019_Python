def quickSort(arr, low, high):
    i = low
    j = high
    if low <= high:
        pivot = arr[i]
        while(i < j):
            while(i < j and arr[j] >= pivot):
                j -= 1
            print(arr, pivot)
            arr[i] = arr[j]

            while(i < j and arr[i] <= pivot):
                i += 1
            arr[j] = arr[i]

        arr[i] = pivot
        quickSort(arr, low, i - 1)
        quickSort(arr, i + 1, high)


array = [2,4,2,14,77,24,2,14]
quickSort(array, 0, len(array) - 1)
print(array)
