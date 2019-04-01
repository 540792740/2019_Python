def BinarySearch(seq, v,):
    left = 0
    right = len(seq)
    while left <= right:
        mid = int((left + right) /2)
        if seq[mid] == v:
            print("Contain")
            break

        elif seq[mid] > v:
            print("1")
            right = mid -1

        elif seq[mid] < v:
            print("2")
            left = mid + 1


    return None

BinarySearch([1,2,3,6,7,8,9], 4)