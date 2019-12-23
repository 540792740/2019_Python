class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T: return []
        stack = [0]
        res = [0] * len(T)
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                temp_index = stack.pop()
                res[temp_index] = i - temp_index
            stack.append(i)

        return res