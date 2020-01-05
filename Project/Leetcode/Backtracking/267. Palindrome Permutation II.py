class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        n = len(s)
        counter = {}
        for c in s: counter[c] = counter.get(c, 0) + 1
        # Count number is Odd
        odd = [key for key, values in counter.items() if values % 2 != 0]

        # Init helper function
        def helper(path):
            if len(path) == n:
                ans.append(path)
                return
            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 2
                    helper(k + path + k)
                    counter[k] += 2

        if len(odd) > 1: return []
        if len(odd) == 1:
            counter[odd[0]] -= 1
            helper(odd[0])
        else:
            helper('')
        return ans



if __name__ == "__main__":
    S = Solution()
    test = S.generatePalindromes('aabbbc')
    print(test)
    test = S.generatePalindromes('aabb')
    print(test)
    test = S.generatePalindromes('cbbbbaaaa')
    print(test)
    test = S.generatePalindromes('a')
    print(test)
    test = S.generatePalindromes('aa')
    print(test)
    test = S.generatePalindromes('aaa')
    print(test)