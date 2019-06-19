class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        ls = len(nums)
        right = ls - 1
        while left < right:
            mid = int((left + right) / 2)
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] < target:
            return left + 1
        return left


if __name__ == '__main__':
    S = Solution()
    a = S.searchInsert([1,3,5,6],0)
    print(a)
