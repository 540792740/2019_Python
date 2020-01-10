class Solution:
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            retirm -1
        pos = 0
        balance = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                pos = i + 1
        return pos

