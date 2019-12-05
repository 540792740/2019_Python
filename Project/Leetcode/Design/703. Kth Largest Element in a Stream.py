import heapq
class KthLargest(object):
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k: heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)

        # Mush using elif, because if len() < k, has been push into nums
        elif val > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)

        print(self.nums)
        return self.nums[0]

if __name__ == '__main__':
    S = KthLargest(3,[4,5,8,2])
    S.add(3)
    S.add(5)
    S.add(10)
    S.add(9)
    S.add(4)
