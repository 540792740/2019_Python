#1 1 2 3 5 8 13,21...
def fibo(n):
    if n > 2: return fibo(n - 1) + fibo(n - 2)
    elif n == 1: return 1
    elif n == 2: return 1
    else: return "error"
nums = []
for i in range(1,20):
    nums.append(fibo(i))
print(nums)

'''
find min fibonacci number small than num
'''
def fibonacci(num):
    if num < 0: return False
    if num < 2: return num
    a, b = 1, 1
    while True:
        print(a)
        a, b = b, a + b
        if b > num:
            return a
print(fibonacci(555))