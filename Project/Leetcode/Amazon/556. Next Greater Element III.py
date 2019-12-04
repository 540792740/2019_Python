'''
Next Permutation.
1237654 -> from right to left, find nums[i] < nums[i + 1]
1234567 -> from i to right, find j larger than nums[i], swap nums[i], nums[j]
1243567
12432 -> 12234 -> 13224

Edge test case:
[], [12345], [2 ** 32]]
'''


def nextGreaterElement(n):
    nums = list(str(n))
    ls = len(nums)
    i = ls - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1
    i = i - 1

    # Reverse worst case is O(n)
    nums[i + 1: ls] = nums[i + 1: ls][::-1]
    print(nums, i)
    for j in range(i + 1, ls):
        if int(nums[j]) > int(nums[i]):
            nums[j], nums[i] = nums[i], nums[j]
            break
    res = ''.join(nums)
    if int(res) >= 2 ** 31 - 1: return -1
    if int(res) > n: return res
    else:return -1

def nextGreaterElement1(n):
    """
    :type n: int
    :rtype: int
    """
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    def reverse(nums, i, j):
        while i < j:
            swap(nums, i, j)
            i += 1
            j -= 1

    nums = list(str(n))
    ls = len(nums) - 1
    i = ls
    while i > 0 and int(nums[i]) <= int(nums[i - 1]):
        i -= 1
    reverse(nums, i, ls)
    if i > 0:
        for j in range(i, ls + 1):
            if int(nums[i - 1]) < int(nums[j]):
                swap(nums, i - 1, j)
                break
    res = ''.join(nums)
    if int(res) >= 2 ** 31 - 1: return -1
    if int(res) > n:
        return res
    else:
        return -1
print(nextGreaterElement(12222333))
# print(nextGreaterElement(1237654))