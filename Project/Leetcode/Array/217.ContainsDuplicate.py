class Solution(object):
    # 95% beat
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums)-len(set(nums))==0):
            return False
        else: return True

    # by me, 67% beat
    def containsDuplicate1(self, nums):
        ls = len(nums)
        dic = {}
        for i in range(ls):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return True

        return False
if __name__ == '__main__':
    S= Solution()
    a = S.containsDuplicate([1,2,3,1,2,4])
    print(a)
