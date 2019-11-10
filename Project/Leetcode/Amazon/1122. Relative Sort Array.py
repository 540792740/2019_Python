class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Save all value into dic
        dic = {}
        for i, u in enumerate(arr1):
            if u not in dic:
                dic[u] = 1
            else:
                dic[u] += 1
        res = []

        # define a function to add number into res
        def add_res(times, res, value):
            while times > 0:
                res.append(value)
                times -= 1
        # add number in arr2 into res
        for i in arr2:
            times = dic[i]
            add_res(times, res, i)
            dic.pop(i)

        # add number not in arr2 but in arr1 into rres
        index = sorted(dic)
        for i in index:
            add_res(dic[i], res, i)
        return res
        return res



