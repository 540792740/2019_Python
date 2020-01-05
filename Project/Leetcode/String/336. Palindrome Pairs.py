class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic, res = {}, []
        dic = {v[::-1] : i for i, v in enumerate(words)}
        # for i, v in enumerate(words): dic[v[::-1]] = i
        for i, s in enumerate(words):
            for j in range(len(s) + 1):
                prefix, postfix = s[:j],s[j:]
                print(s, prefix, postfix)

                # Prefix match to another word, Postfix is palindrome
                if prefix in dic and i != dic[prefix] and postfix == postfix[::-1]:
                    res.append([i, dic[prefix]])

                #  Postfix mach to another word, Prefix is palindrome
                if j > 0 and postfix in dic and i != dic[postfix] and prefix == prefix[::-1]:
                    res.append([dic[postfix], i])
                    
        return res


if __name__ == '__main__':
    S = Solution()
    test = S.palindromePairs(["abcd","dcba","lls","s","sssll"])
    print(test)