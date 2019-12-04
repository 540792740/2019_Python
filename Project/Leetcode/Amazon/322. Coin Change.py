'''
Before coding, i have some questions of this problem

question:
1.  Is the list coins is sorted?

2.  Could i Assume that the the amount will not exceed largest integer 2 power of 31
    Actually, in Python there is not a big deal, but in Java, largest is 2^31 -1

3.  Test edge: [],1  [2],1  [2],2   [1,2,3], 14

'''
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






# Wrong answer!!!!!!!!!!!!!!!
def coinChange1(coins, amount):
    coins.sort()
    res = 2 ** 31 - 1
    coin_list = []
    def dfs(coins, path):
        if path not in coin_list and path: coin_list.append(path)
        for i in range(len(coins)):
            dfs(coins[i + 1:], path + [coins[i]])
    dfs(coins, [])
    for coin in coin_list:
        count = 0
        temp = amount
        for i in range(len(coin) - 1, -1, -1):
            count += temp // coin[i]
            temp %= coin[i]
        if temp > 0 or count == 0: count = 2 ** 31 - 1
        res = min(count, res)
    if res == 2 ** 31 - 1: return -1
    return res
# print(coinChange([1,2,5], 11))
print(coinChange([186,419,83,408], 6249))
# print(coinChange([1,2,3,4], 69))