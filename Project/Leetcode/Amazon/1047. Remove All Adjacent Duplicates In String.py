class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        ls = len(S)
        if ls <= 1: return S
        check_dup = S[0]
        stack = [S[0]]
        for i in range(1, ls):
            if check_dup == S[i]:
                stack.pop()
                if stack:
                    check_dup = stack[-1]
                else:
                    check_dup = -1
            else:
                stack.append(S[i])
                check_dup = S[i]
        return ''.join(stack)