def numRollsToTarget( d, f, target):
    """
    :type d: int
    :type f: int
    :type target: int
    :rtype: int
    """
    if d > target or d * f < target: return 0
    dp = [[0] * (d * f + 1) for i in range(d)]
    for i in range(1, f + 1):
        dp[0][i] = 1
    for i in range(1, d):
        for j in range(d * f + 1):

            # This time, the number of dice rolled
            for k in range(1, f + 1):
                dp[i][j] += dp[i - 1][j - k]
                print(dp)
    return dp[-1][target] % (10 ** 9 + 7)


numRollsToTarget(3, 3, 5)
