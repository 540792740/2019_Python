class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = set()
        for i in nums:
            if i in dic:
                dic.remove(i)
            else:
                dic.add(i)
        return list(dic)[0]


    def singleNumber1(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)