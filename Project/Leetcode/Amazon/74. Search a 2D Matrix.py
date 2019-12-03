def searchMatrix(matrix, target):
    # Binary Search O(log(n))
    m = len(matrix)
    if m == 0: return False
    n = len(matrix[0])
    if n == 0: return False
    l, r = 0, m * n - 1
    while l <= r:
        mid = (l + r) // 2
        print(mid)
        if matrix[mid // n][mid % n] == target:
            return True
        elif matrix[mid // n][mid % n] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))

# 76%
# from right top to left bottom O(n)
def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0: return False
    n = len(matrix[0])
    if n == 0: return False
    i, jx = 0, n - 1
    while i < m:
        for j in range(jx, -1, -1):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                continue
            else:
                jx = j
                break
        i += 1
    return False
