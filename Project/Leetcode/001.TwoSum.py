'''
123
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls = len(nums)
        for i in range(0,ls-1):
            print(i)
            for j in range(i + 1, ls):
                if nums[i] + nums[j] ==target:
                    return [i,j]
test
'''
# 指针：
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_index = [(index, i) for i, index in enumerate(nums)]
        nums_index.sort()
        print(nums_index)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums_index[left][0] + nums_index[right][0] == target:
                return [nums_index[left][1] ,nums_index[right][1]]
            elif nums_index[left][0] + nums_index[right][0] > target:
                right -= 1
            else:
                left += 1

if __name__ =='__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))