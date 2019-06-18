'''
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

'''
# 指针：
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0,len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return[nums_index[begin][1],nums_index[end][1]]
            elif curr > target:
                end -= 1
            else:
                begin += 1
        print(nums_index)


if __name__ =='__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))