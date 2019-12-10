'''
Question:
1.  input list of integer?
2.  Output element
3.  How many duplicate? just one or return all


Solve:
1.  Using set to solve
2.  Write a loop, in dic, return, or add to set
3.  Complexity should be O(n)
'''

class Solution:
    def findDuplicate(self, nums):
        class Solution:
            def findDuplicate(self, nums: List[int]) -> int:
                dic = {}
                for i in range(len(nums)):
                    if nums[i] not in dic:
                        dic[nums[i]] = 1
                    else:
                        return nums[i]
                return -1