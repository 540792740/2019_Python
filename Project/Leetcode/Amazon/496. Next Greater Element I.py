def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # Init res[] and stack[]
    res, stack = [], []

    # Init dic save next element:
    dic = {}
    for element in nums2:
        while stack and element > stack[-1]:
            dic[stack.pop()] = element
        stack.append(element)
    for element in nums1:
        res.append(dic.get(element, -1))
    return res

if __name__ == '__main__':
    print(nextGreaterElement([4,1,2], [1,3,4,2]))