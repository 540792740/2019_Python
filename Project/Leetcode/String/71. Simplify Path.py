class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [p for p in path.split("/") if p != "." and p != ""]
        print(places)
        stack = []
        for element in places:
            if element =='..':
                if stack: stack.pop()
            else:
                stack.append(element)
        return '/' + '/'.join(element)

if __name__ == '__main__':
    S = Solution()
    test = S.simplifyPath("/a/../../b/../c//.//")
    print(test)