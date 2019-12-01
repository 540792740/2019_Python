
O(N)
def maximumProduct(self, nums):
    a, b, c = heapq.nlargest(3, nums)
    e, f = heapq.nsmallest(2, nums)
    return max(a * b * c, e * f * a)

# O(nlogn)
def maximumProduct(self, nums):
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])