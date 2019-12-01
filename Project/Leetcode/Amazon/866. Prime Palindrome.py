'''
length of return element must be odd:
1221, 1331, 2332, --> all can be divided by 11.
--> return type aba

'''
def primePalindrome(N):
    while N <= 11:
        if N in [2, 3, 5, 7, 11]:
            return N
        else:
            N += 1
    def palindromes(n):
        l = n // 2
        for i in range(10 ** (l - 1), 10 ** l):
            s = str(i)
            for j in range(10):
                yield int(s + str(j) + s[::-1])

    def is_prime(n):
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                return False
        return True
    ls = len(str(N))
    while True:
        for x in palindromes(ls):
            if x >= N and is_prime(x):
                return x
        ls += 1
print(primePalindrome(99999))


# 30%
def primePalindrome1(N):
    def reverse(n):
        return int(str(n)[::-1])

    def is_prime(n):
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                return False
        return True

    if N in [0, 1]: return 2
    while True:
        if N == reverse(N) and is_prime(N):
            return N
        N += 1
# print(primePalindrome1(55))
# print(primePalindrome1(1))




def reverse(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n //= 10
    return res
