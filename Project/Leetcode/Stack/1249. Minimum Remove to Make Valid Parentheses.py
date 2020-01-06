class Solution:
    def minRemoveToMakeValid(self, s):
        remove_Pos = set()
        left = []
        for i, c in enumerate(s):
            if c == '(': left.append(i)
            elif c == ')':
                if left: left.pop()
                else:
                    remove_Pos.add(i)
        remove_Pos = remove_Pos | set(left)
        print(remove_Pos, left)
        return ''.join(c for i, c in enumerate(s) if i not in remove_Pos)

if __name__ == '__main__':
    S = Solution()
    # test = S.minRemoveToMakeValid('lee(t(c)o)de)')
    test = S.minRemoveToMakeValid("))((")
    print(test)
