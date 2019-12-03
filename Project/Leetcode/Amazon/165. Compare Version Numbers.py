def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    # O(n)
    version1 = [int(v) for v in version1.split(".")]
    version2 = [int(v) for v in version2.split(".")]
    ls1 = len(version1)
    ls2 = len(version2)
    ls = ls1 - ls2
    version1 += [0] * (-ls)
    version2 += [0] * (ls)
    for i in range(len(version1)):
        if version1[i] < version2[i]:
            return -1
        elif version1[i] > version2[i]:
            return 1
    return 0

print(compareVersion("01", "1"))
print([0] * -2)