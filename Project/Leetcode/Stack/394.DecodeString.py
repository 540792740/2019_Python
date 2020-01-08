'''
0. Build an array store [alpha, number, FinalString]
1. when meet alpha, number, save
2. when meet '[', save [a, n, final]
3. when meet ']', pop last array, read finalstring and save.
'''

# O(n), traverse all character
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1, '']]
        a = n = ''
        for c in s:
            if c.isalpha():
                a += c
            elif c.isdigit():
                n += c
            elif c == '[':
                stack.append([a, int(n), ''])
                a = n = ''
            else:
                p, t, b = stack.pop()
                stack[-1][-1] += p + t * (b + a)
                a = ''

        return stack.pop()[-1] + a

if __name__ == '__main__':
    S = Solution()
    # a = S.decodeString("3[a]2[bc]")
    # a = S.decodeString("3[a2[c]]")
    a = S.decodeString("3[a]2[b4[F]c]")
    print(a)
    # b = [['AF', 1, 'WW'], [a, 1, 'DS']]
    # print(b[-1][-1])
