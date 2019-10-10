class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while(left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


if __name__ == '__main__':
    S = Solution()
    a = S.reverseString(["h","e","l","l","o"])
    print(a)