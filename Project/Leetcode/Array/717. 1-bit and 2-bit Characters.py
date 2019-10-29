'''
This question is Error
'''

class Solution:
    def isOneBitCharater(self, b):
        ls = len(b) - 1
        i = 0
        while i < ls:
            i += 1 + b[i]
            if i == ls:
                return True
            else:
                return False