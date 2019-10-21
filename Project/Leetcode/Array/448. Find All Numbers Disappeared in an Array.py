class Solution(object):
    def findDisappearedNumbers1(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))


    # brust: it works but too slow.
    # I change list in to set can efficient save time to 84%
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        ls = len(set(nums))
        S = set(nums)
        miss_number = len(nums) - ls
        for i in range(1, len(nums) + 1):
            if i not in S and miss_number > 0:
                res.append(i)
                miss_number -= 1
        return res
if __name__ == '__main__':
    S = Solution()
    test = S.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    # test = S.findDisappearedNumbers([1,1])
    print(test)