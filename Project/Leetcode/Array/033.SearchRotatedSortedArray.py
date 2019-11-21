class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ls = len(nums)
        l, r = 0, ls - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[l] == target: return l
            if nums[r] == target: return r

            # Left sorted
            if nums[mid] > nums[l]:
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == '__main__':
    s= Solution()
    # s.search([4,5,6,7,0,1,2], 0)
    a = s.search([5, 1,3], 0)
    print(a)