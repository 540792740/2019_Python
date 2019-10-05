class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1, '']]
        a = n = ''
        res = ''
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
    a = S.decodeString("3[a]2[bc]")
    print(a)
    b = [['', 1, ''], [a, 1, '']]
    print(b.pop())
