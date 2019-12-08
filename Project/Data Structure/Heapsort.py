def heapsort(nums):
    ls = len(nums)

    # build max-heap
    for i in range(ls // 2 - 1, -1, -1):
        heapify(nums, ls, i)
    print(nums)
    # Swap
    for i in range(ls - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
        print('nums', nums)
def heapify(nums, ls, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < ls and nums[i] < nums[l]:
        largest = l
    if r < ls and nums[largest] < nums[r]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]  # 交换

        # find next max value based on node nums[largest] which has been swapped
        heapify(nums, ls, largest)

a = [2,6,8,2,5,7,1,9]
heapsort(a)


from heapq import heappop, heappush
def heap_sort(nums):
    res = []
    for value in nums:
        heappush(res, value)
    return [heappop(res) for i in range(len(res))]
# print(heap_sort(a))