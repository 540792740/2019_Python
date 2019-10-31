class Solution:
    # 92%
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        #       when there is no number in one or two lists, always return []
        if not nums1 or not nums2:
            return []

        #       Save one list into list
        dic = {}
        for n in nums1:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        #       find all possible value in another list
        for i in nums2:
            if i in dic:
                res.append(i)
                if dic[i] == 1:
                    dic.pop(i)
                elif dic[i] > 1:
                    dic[i] -= 1
        return res