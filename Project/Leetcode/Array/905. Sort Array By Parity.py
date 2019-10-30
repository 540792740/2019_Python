class Solution:
    # 95%
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] % 2 == 0:
                l += 1
            else:
                A[l], A[r] = A[r], A[l]
                r -= 1
        return A