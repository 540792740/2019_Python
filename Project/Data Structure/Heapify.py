'''
for a binary tree, First root is index / 2
'''


class MaxHeap:
    def __init__(self, nums):
        self.capacity = len(nums)
        self.data = [None] * (self.capacity + 1)
        self.count = len(nums)
        self. __heapify(nums)
    def __heapify(self, nums):
        # value one by one
        for i in range(self.capacity):
            self.data[i + 1] = nums[i]
        for i in range(self.count // 2, 0, -1):
            self.sink(i)
        print(nums)

if __name__ == '__main__':
    S = MaxHeap([2,7,4,1,8,1])
    # print(S)