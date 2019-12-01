def lengthLongestPath(input):
    """
    :type input: str
    :rtype: int
    """
    stack = [(-1, 0)]
    max_len = 0
    for p in input.split('\n'):
        depth = p.count('\t')
        p = p.replace('\t', '')
        while stack and depth <= stack[-1][0]:
            stack.pop()
        if '.' not in p:
            stack.append((depth, len(p) + stack[-1][1] + 1) )
        else:
            max_len = max(max_len, len(p) + stack[-1][1])
    return max_len


lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")