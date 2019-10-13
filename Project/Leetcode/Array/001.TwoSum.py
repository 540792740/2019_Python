'''
0. New dic
1. Find wanted num and save in dic
2. check whether on target
3. return [tag, tag], careful the return content, not value, the tag
'''
# 指针：
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls = len(nums)
        wanted_nums = {}
        for i in range(ls):
            if nums[i] not in wanted_nums:
                wanted_nums[target - nums[i]] = i
            else:
                # return 0
                return [wanted_nums[nums[i]], i]

if __name__ =='__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))