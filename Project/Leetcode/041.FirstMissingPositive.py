class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        FirstValue = 1
        for i in nums:
            if i > FirstValue:
                return FirstValue
            else:
                if i == FirstValue:
                    FirstValue += 1
        return FirstValue
if __name__ == '__main__':
    S = Solution()
    a = S.firstMissingPositive([-5])
    a = S.firstMissingPositive([1,2,0])
    a = S.firstMissingPositive([2147483647])
    print(a)