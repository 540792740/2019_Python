def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # length must larger than 2
    ls = len(nums)
    if ls <= 2: return False

    # Init index_3
    num_third = -float(2 ** 31 - 1)

    # Init stack to find index_2, index_1:
    stack = [nums[-1]]
    for i in range(ls - 2, -1, -1):
        # nums[i] is num_first
        if nums[i] < num_third:
            return True

            # Find num_second(nums[i]) > num_third.
        # pop third, then find num_first
        else:
            while stack and nums[i] > stack[-1]:
                num_third = stack.pop()
        stack.append(nums[i])
    return False

# print(find132pattern([1,2,3,4]))
print(find132pattern([-1, 3, 2, 0]))
