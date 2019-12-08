'''
Longest Common String
         J  i  a  J  i  a
    [[0, 0, 0, 0, 0, 0, 0],
   J [0, 1, 0, 0, 1, 0, 0],
   i [0, 0, 2, 0, 0, 2, 0],
   a [0, 0, 0, 3, 0, 0, 3],
   W [0, 0, 0, 0, 0, 0, 0],
   e [0, 0, 0, 0, 0, 0, 0],
   i [0, 0, 1, 0, 0, 1, 0]]

'''
def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    longest = 0
    if m < 0 or n < 0:return 0
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                longest = max(longest, matrix[i][j])
    print(matrix)
    return longest


print(LCS('Jiawei', 'JiaJia'))