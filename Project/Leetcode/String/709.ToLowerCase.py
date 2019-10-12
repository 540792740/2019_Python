class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        ans = ''
        for s in str:
            if ord(s) >= ord('A') and ord(s) <= ord('Z'):
                ans += chr(ord(s) - (ord('A') -ord('a')))
            else:
                ans += s
        return ans

    def toLowerCase1(self, str):
        return str.lower()