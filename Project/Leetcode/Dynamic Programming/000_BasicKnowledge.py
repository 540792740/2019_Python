'''
Dynamic programming contains 2 parts:

Longest Common Subsequence,LCS

Pack:
'''

class basic(object):
    def LCS(self,s1, s2):
        length1 = len(s1)
        length2 = len(s2)
        matrix = [[0]*(length1 + 1)]* (length2 + 1)
        print(matrix)
        L_str = 0
        last_number = 0
        for i in range(length1):
            for j in range(length2):
                if s1[i] == s2[j]:
                    matrix[i + 1][j + 1] = matrix[i][j] + 1
                    if matrix[i + 1][j + 1] > L_str:
                        L_str = matrix[i + 1][j + 1]
                        last_number = i + 1
        return s1[last_number - L_str:last_number]


if __name__ == "__main__":
    S = basic()
    a = S.LCS('abcj','jabcs')
    print(a)
