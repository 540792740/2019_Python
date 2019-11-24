import collections
class Solution:
    def subarraySum(self, nums, k) :
        n = len(nums)
        dic = collections.defaultdict(int)
        dic[0] = 1
        summary, res = 0, 0
        for n in nums:
            summary += n
            if dic[summary - k]:
                res += dic[summary - k]
            dic[summary] = dic.get(summary, 0) + 1
        return res


if __name__ == '__main__':
    S = Solution()
    test = S.subarraySum([1,2,3,1], 3)
    print(test)
    test = S.subarraySum([0,0,0,0,0,0], 0)
    print(test)

