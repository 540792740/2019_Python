import heapq
def maximumMinimumPath(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    # Init directions
    direction = ((1,0),(0,1),(-1,0),(0,-1))

    # Init length of the matrix A
    m = len(A)
    n = len(A[0])

    # Init matrix visited to record visited or not, 0 means not visited
    visited = [[0 for _ in range(n)] for _ in range(m)]

    # Init queue
    queue = [(-A[0][0], 0, 0)]

    while queue:

        # heappop the max value in the queue
        element, x, y = heapq.heappop(queue)

        # At the end of the matrix A
        if x == m - 1 and y == n - 1:
            return -element

        # DFS find all possible element
        for dx, dy in direction:
            dx = x + dx
            dy = y + dy

            # Traverse all not visited element
            if -1 < dx < m and  -1 < dy < n and visited[dx][dy] == 0:
                visited[dx][dy] = 1

                # heappush, save the first element as the maximum min value
                heapq.heappush(queue, (max(-A[dx][dy], element), dx, dy))

# print(maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]))
print(maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]]))