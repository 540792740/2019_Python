class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        N = len(deck)
        res = [0] * N
        que = collections.deque()
        for i in range(N):
            if que:
                que.appendleft(que.pop())
            que.appendleft(deck.pop())
        return list(que)