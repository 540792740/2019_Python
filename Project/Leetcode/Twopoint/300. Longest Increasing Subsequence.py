class Solution:

    # DP Regular
    def lengthOfLIS1(self, nums):
        if nums == []: return 0
        ls = len(nums)
        dp = [1] * ls
        for i in range(1, ls):
            temp = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j] + 1)
            dp[i] = temp
        return max(dp)

    # Two pointer Faster
    def lengthOfLIS(self, nums):
        ls = len(nums)
        tails = [0] * ls
        size = 0
        for x in nums:
            l, r = 0, size
            while l != r:
                m = (l + r) // 2
                if tails[m] < x:
                    l = m + 1
                else:
                    r = m
            tails[l] = x
            print(tails)
            size = max(size, l + 1)
        return size

if __name__ == '__main__':
    S = Solution()
    test = S.lengthOfLIS([10,9,2,5,6,3,7,101,18,2,7,8,9,10,11,12])
    # test = S.lengthOfLIS1([10,9,2,5,6,3,7,101,18])
    # test = S.lengthOfLIS1([1,3,6,7,9,4,10,5,6])
    print(test)