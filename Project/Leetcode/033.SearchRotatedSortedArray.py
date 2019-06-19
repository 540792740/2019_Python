class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ls = len(nums)
        def get(start, end):
            if start > end:
                return -1
            mid = int((start + end) / 2)
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[start]: #first part is sorted
                if target < nums[mid] and target >= nums[start]:
                    if target == nums[start]:
                        return start
                    else:
                        return get(start, mid -1)
                else:
                    return get(mid + 1, end)
            elif nums[mid] <= nums[end]:     #Second part is sorted
                if target <= nums[end] and target > nums[mid]:
                    if target == nums[end]:
                        return end
                    else:
                        return get(mid + 1,end)
                else:
                    return get(start, mid - 1)

        return get(0,ls - 1)

if __name__ == '__main__':
    s= Solution()
    # s.search([4,5,6,7,0,1,2], 0)
    a = s.search([5, 1,3], 0)
    print(a)