import heapq
class Solution:

    # sort()
    def findKthLargest1(self, nums, k):
        ls = len(nums)
        if ls < k: return
        nums.sort(reverse = True)
        return nums[k - 1]

    # Merge sort: 30% nlogn
    def findKthLargest2(self, nums, k):

        def merge(l, r):
            res = []
            while l and r:
                if l[0] > r[0]: res.append(l.pop(0))
                else: res.append(r.pop(0))
            res += l + r
            return res

        def mergeSort(nums):
            ls = len(nums)
            if ls <= 1: return nums
            mid = ls // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)

        nums = mergeSort(nums)
        return nums[k - 1]

    # Quick sort
    def findKthLargest3(self, nums, k):
        def quickSort(nums, low, high):

            i = low
            j = high

            if low <= high:
                pivot = nums[low]
                while i < j:
                    while i < j and nums[j] <= pivot:
                        j -= 1

                    nums[i], nums[j] = nums[j], nums[i]

                    while i < j and nums[i] >= pivot:
                        i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                nums[i] = pivot
                quickSort(nums, low, i - 1)
                quickSort(nums, i + 1, high)
        quickSort(nums, 0, len(nums) - 1)
        return nums[k - 1]

    # Heapify nlogn
    def findKthLargest4(self, nums, k):
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)

if __name__ == '__main__':
    S = Solution()
    test = S.findKthLargest4([3,2,1,5,6,4],2)
    print(test)
    x = {'foo': 'bar'}
    y = {'bar':x}
    z = y['bar']['foo']
    print(z)

    print(sum(x * x for x in [1, 2, 3]))