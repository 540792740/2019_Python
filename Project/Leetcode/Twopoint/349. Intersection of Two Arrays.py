class Solution:
    def intersection(self, nums1, nums2):
        res = set()

        #       when there is no number in one or two lists, always return []
        if not nums1 or not nums2:
            return []

        #       Save one list into list
        dic = {}
        for n in nums1:
            if n not in dic:
                dic[n] = n
            else:
                continue

        #       find all possible value in another list
        for i in nums2:
            if i in dic:
                res.add(i)
            if len(res) == len(dic):
                return res
        return res