class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums)-len(set(nums))==0):
            return False
        else: return True

if __name__ == '__main__':
    S= Solution()
    a = S.containsDuplicate([1,2,3,1,2,4])
    print(a)
