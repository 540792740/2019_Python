class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key,[]) + [w]
            print(d[key])
        return d.values()

if __name__ == '__main__':
    S = Solution()
    a = S.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(a)





