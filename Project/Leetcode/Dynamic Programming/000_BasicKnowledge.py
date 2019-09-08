'''
Dynamic programming contains 2 parts:

Longest Common Subsequence,LCS

Pack:
'''

class basic(object):
    def LCS(self,s1, s2):
        length1 = len(s1)
        length2 = len(s2)
        matrix = [[0]*(s1 + 1)]*(s2 + 1)
        print(matrix)

        return

if __name__ == "__main__":
    S = basic()
    S.LCS('abcj','jabcs')

