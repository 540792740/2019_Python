class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        i = 0
        while i < len(ransomNote):
            if ransomNote[i] not in magazine:
                return False
            magazine = magazine.replace(ransomNote[i], '')
            i += 1
        return True


if __name__ == '__main__':
    S = Solution()
    a = S.canConstruct("abcdd", "babcsdd")
    print(a)