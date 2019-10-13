'''
i = 0
j = i + 1
k = len() -1
make sure to avoid duplicate result.
'''

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        ls = len(nums)
        for i in range(ls - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = ls - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] ==nums[right -1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        list = []
        if len(nums) <= 2:
            return list
        else:
            k = len(nums) - 1
            for i in range(0,len(nums) - 1):
                k = len(nums) - 1
                if nums[i] == nums[i - 1] and i > 0:
                    i += 1
                    continue;
                j = i + 1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        list.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while (nums[j] == nums[j - 1] and nums[k] == nums[k + 1] and j < k):
                            j += 1
                    elif sum < 0:
                        j += 1
                        while nums[j] == nums[j - 1] and j < k:
                            j += 1
                    else:
                        k -= 1
                        while nums[k] == nums[k + 1] and j < k:
                            k -= 1
        print(list)
        return list



if __name__ == '__main__':
    S = Solution()
    a = S.threeSum([-1, 0, 1, 2, -1, -4])
    # S.threeSum([-2,-3,0,0,-2])
    # S.threeSum([0,0,0])

    print(a)