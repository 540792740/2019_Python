
def nextGreaterElements(nums):
    res = [-1] * len(nums)
    stack = []

    # Search in circularly
    for _ in range(0, 2):
        for i in range(len(nums)):
            while stack and (nums[i] > nums[stack[-1]]):
                res[stack.pop()] = nums[i]
            stack.append(i)
            print(res, stack)

    return res

def nextGreaterElements1(nums):
    prev_l = len(nums)
    nums = nums + nums
    stack = []
    ans = [-1] * len(nums)
    for i, n in enumerate(nums):
        while stack and stack[-1][1] < n:
            prev_i = stack.pop()[0]
            ans[prev_i] = n
        stack.append([i, n])

    return ans[:prev_l]

if __name__ == '__main__':
    print(nextGreaterElements([1,2,1]))
    # print(nextGreaterElements1([1,2,1]))