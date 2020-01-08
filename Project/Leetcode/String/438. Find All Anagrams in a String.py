class Solution(object):
    def findAnagrams(self, s, p):
        dic, temp = {}, {}
        for c in p: dic[c] = dic.get(c, 0) + 1
        res, res_index = [], 0
        ls_s, ls_p = len(s) - 1, len(p) - 1
        # Slide windows
        for c in range(ls_s + 1):
            if s[c] not in dic:
                res_index = c + 1
                temp = {}
            else:
                temp[s[c]] = temp.get(s[c], 0) + 1
                if c - res_index == ls_p:
                    if temp == dic: res.append(res_index)
                    temp[s[res_index]] -= 1
                    if temp[s[res_index]] == 0: del temp[s[res_index]]
                    res_index += 1
        return res

S = Solution()
test = S.findAnagrams("cbaebabacd", "abc")
print(test)