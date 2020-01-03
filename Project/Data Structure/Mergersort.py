def mergeSort(lists):
    ls = len(lists)
    if ls <= 1: return lists
    mid = ls // 2
    left = mergeSort(lists[:mid])
    right = mergeSort(lists[mid:])
    return merge(left, right)

def merge(l, r):
    res = []
    while l and r:
        if l[0] < r[0]: res.append(l.pop(0))
        else: res.append(r.pop(0))
    res += l + r
    return res

print(mergeSort([5,3,7,2,9,1,7]))