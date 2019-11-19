class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in arr1:
            dic[i] = dic.get(i, 0) + 1
        res = []
        for i in arr2:
            res.extend([i] * dic[i])
            for _ in range(dic[i]):
                arr1.remove(i)
        res.extend(sorted(arr1))
        return res


