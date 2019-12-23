'''
1.  For this question, Firstly, I will traverse nums2, save each element into a dic, key is the
    element, value is next greater number
    a)  Use stack, [2, 1, 3]. traverse list, element is larger than previous element, add
        into dic[previous_element] = element
2.  Traverse nums1, save the next greater number of each element in nums1 into a list
3.  return the result list

'''
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
        stacprintk.append(element)
        (stack)

    for element in nums1:
        res.append(dic.get(element, -1))
    return res

if __name__ == '__main__':
    print(nextGreaterElement([4,1,2], [1,3,4,2]))