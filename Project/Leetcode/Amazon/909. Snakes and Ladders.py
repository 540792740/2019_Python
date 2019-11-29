import collections
def snakesAndLadders(board):
    ls = len(board)

    # Function get index of col and row
    def get(s):
        quot, rem = divmod(s - 1, ls)
        row = ls - 1 - quot
        if row % 2 == ls % 2:
            col = ls - rem - 1
        else:
            col = rem
        return row, col

    dist = {1 : 0}
    queue = collections.deque([1])
    while queue:
        s = queue.popleft()

        if s == ls ** 2:
            return dist[s]

        for s2 in range(s + 1, min(s + 6, ls ** 2) + 1):
            row, col = get(s2)
            if board[row][col] != -1:
                s2 = board[row][col]
            if s2 not in dist:
                dist[s2] = dist[s] + 1
                queue.append(s2)
    return -1
if __name__ == '__main__':
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]]
    print(snakesAndLadders(board))
    board = [
        [-1, -1, 19, 10, -1],
        [ 2, -1, -1,  6, -1],
        [-1, 17, -1, 19, -1],
        [25, -1, 20, -1, -1],
        [-1, -1, -1, -1, 15]]
    print(snakesAndLadders(board))
