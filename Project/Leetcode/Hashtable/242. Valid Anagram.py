class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for j in t:
            if j not in dic or dic[j] == 0: return False
            dic[j] -= 1
        for i in dic.values():
            if i > 0: return False
        return True