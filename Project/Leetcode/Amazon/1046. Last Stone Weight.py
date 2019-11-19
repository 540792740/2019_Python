import heapq,bisect
class Solution(object):
    # Complexity N ^ 2, 99%
    def lastStoneWeight(self, A):
        pq = A
        pq = [-x for x in A]
        heapq.heapify(pq)
        for i in range(len(A) - 1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x - y))
        return -pq[0]

    # complexity (nlogn) faster
    def lastStoneWeight1(self, A):
        A = sorted(A)
        for _ in range(len(A) - 1):
            x, y = A.pop(), A .pop()
            bisect.insort(A, x - y)
        return A.pop()

if __name__ == '__main__':
    S = Solution()
    test = S.lastStoneWeight([2,7,4,1,8,1])
    test = S.lastStoneWeight([2,6,3,9,9,3,8])
    test = S.lastStoneWeight1([2,6,3,9,9,3,8])
    print(test)
    a = [1,1,2,2,3,3,3]
    a.pop()
    print(a)