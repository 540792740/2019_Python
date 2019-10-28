class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_exist = set()
        res = []
        for i in nums:
            if i not in num_exist:
                num_exist.add(i)
            else:
                res.append(i)
        return res