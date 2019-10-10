'''


'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0 and len(s) != 0:
            return False
        else:
            pars = [None]
            parmap = {')':'(', '}':'{',']':'['}
            for c in s:
                if c in parmap and parmap[c] == pars[len(pars) - 1]:
                    a = pars.pop()
                else:
                    pars.append(c)
        print(pars)
        return len(pars) == 1
if __name__ == '__main__':
    S = Solution()
    a = S.isValid("([])")
    print(a)