'''
Solution: https://blog.csdn.net/fuxuemingzhu/article/details/79473171
'''
def findMaximumXOR(nums):
    ans = mask = 0
    for x in range(32)[::-1]:
        mask += 1 << x
        print(bin(mask), x)
        prefixSet = set([n & mask for n in nums])
        print(prefixSet)
        temp = ans | 1 << x
        print('temp', bin(temp))
        for prefix in prefixSet:
            if temp ^ prefix in prefixSet:
                ans = temp
                break
    return ans
findMaximumXOR([3, 10, 5, 25, 2, 8])


# RTL O(n^2)
import heapq
def findMaximumXOR1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    ls = len(nums)
    for i in range(ls - 1):
        for j in range(i, ls):
            if nums[i] ^ nums[j] > res: res = nums[i] ^ nums[j]
    return res
# findMaximumXOR1([3, 10, 5, 25, 2, 8])