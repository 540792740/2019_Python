
'''
nums = [6,9,7,4,2]:
Algorithm is update second value.
Reverse order
when 2 < 4: we need find s1 < 2.
when 7 < 9: update, find s1 < 7

'''
def find132pattern1(nums):
    stack = []
    s3 = -2 ** 31
    for n in nums[::-1]:
        if n < s3: return True
        while stack and stack[-1] < n:
            s3 = stack.pop()
        stack.append(n)
    return False

# print(find132pattern([1,2,3,4]))
print(find132pattern1([-1, 3, 2, 0]))
