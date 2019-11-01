class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    print(j,m)
                    j = m
            tails[i] = x
            print(tails)
            size = max(i + 1, size)
        return size

if __name__ == '__main__':
    S = Solution()
    test = S.lengthOfLIS([10,9,2,5,6,3,7,101,18])
    print(test)