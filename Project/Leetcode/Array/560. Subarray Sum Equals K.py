class Solution:
    def subarraySum(self, nums, k) :
        count = 0
        summary = 0
        dic = {}
        dic[0] = 1
        for i in range(len(nums)):
            summary += nums[i]
            count += dic.get(summary - k, 0)
            # d[summary] = d.get(summary, 0) + 1
            if summary in dic: dic[summary] += 1
            else: dic[summary] = 1
        return count
if __name__ == '__main__':
    S = Solution()
    test = S.subarraySum([1,2,3,1], 3)
    print(test)
    test = S.subarraySum([0,0,0,0,0,0], 0)
    print(test)

