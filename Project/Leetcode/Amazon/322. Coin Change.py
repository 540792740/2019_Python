'''
Before coding, i have some questions of this problem

question:
1.  Is the list coins is sorted?

2.  Could i Assume that the the amount will not exceed largest integer 2 power of 31
    Actually, in Python there is not a big deal, but in Java, largest is 2^31 -1

3.  Test edge: [],1  [2],1  [2],2   [1,2,3], 14

'''
# DP
def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    if dp[amount] == amount + 1: return -1
    else: return dp[amount]



# DFS
def coinChange(coins, amount):
    coins.sort(reverse = True)
    ls, res = len(coins), 2 ** 31 - 1

    def dfs(index, rem, count):
        nonlocal res
        if not rem: res = min(res, count)
        for i in range(index, ls):
            if coins[i] <= rem < coins[i] * (res - count):
                dfs(i, rem - coins[i], count + 1)
    for i in range(ls):
        dfs(i, amount, 0)
    if res == 2 ** 31 - 1: return -1
    else: return res





