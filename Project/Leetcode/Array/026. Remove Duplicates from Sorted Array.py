class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = len(nums)
        if ls <= 1:
            return ls
        i = 0
        res = [nums[0]]
        while i + 1 < ls:
            if nums[i] == nums[i + 1]:
                i += 1
            else:
                res.append(nums[i + 1])
                i += 1
        return res

if __name__ == '__main__':
    S = Solution()
    a = S.removeDuplicates([1,1,2])
    print(a)