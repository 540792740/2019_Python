'''
Question:
1.  Is there will have element which is smaller than 0, Negative number
2.  The largest number in the list, what will return? minus 1 (-1)?
3.  When is comes to the last element in the list, I need to search circularly right?


Answer:
1.  For this question, target is to find nex greater element in the list, I will stack
    to solve the problem, save small element into stack, when find element which is larger
    than stack[-1], return the element as the next larger number of stack[-1]

2.  Edge test case: [], [3, 2, 1], [1, 2, 3], [2, 2, 2]

Follow up:
1.  Any other way?
    a)  I believe I could save into a dic when I traverse all element, but the space complexity will
        larger, I don't think it is a good way compare with this way. but it can solve the problem.
2.  Complexity:
    a)

'''
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