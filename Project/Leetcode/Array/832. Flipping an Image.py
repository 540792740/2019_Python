class Solution:

    # Simple way, no need to discuss odd or even, just [::-1]
    # value is equal to 1 - x
    def flipAndInvertImage(self, A):
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                A[i][j] = 1 - A[i][j]
        return [i[::-1] for i in A]

    # 98% bymyself
    def flipAndInvertImage1(self, A):
        # 1. reverse & invert in 1 loop
        m, n = len(A), len(A[0])
        # invert function
        def invert(A, i, j):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0
        # swap function
        def swap(A, i, j, n):
            A[i][j], A[i][n - 1 - j] = A[i][n - 1 - j], A[i][j]

        for i in range(m):
            for j in range(n):
                print(A)
                # even number in list
                if n % 2 == 0:
                    # Mid number in list, return to next loop list
                    if j == n // 2 :
                        break
                    # Swap and invert
                    else:
                        invert(A, i, j)
                        invert(A, i, n - 1 - j)
                        swap(A, i, j, n)
                # odd number in list
                else:
                    if j == n // 2:
                        invert(A, i, j)
                        break
                    else:
                        invert(A, i, j)
                        invert(A, i, n - 1 - j)
                        swap(A, i, j, n)
        return A
if __name__ == '__main__':
    S = Solution()
    test = S.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
    print(test)