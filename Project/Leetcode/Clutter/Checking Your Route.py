
class Solution(object):

    def minimumCost(self, start, end, N, connections):
        # Using DP to solve the problem
        # Init a matrix, save all connection into matrix
        matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for i, j, cost in connections:
            matrix[i][j] = cost
            matrix[j][i] = cost
        self.min_cost = 2**31 - 1
        self.min_cost_path = []

        # Function dfs, find min cost path
        def dfs(start, path, cur_cost):

            # Break when path cost more than minimum cost
            if cur_cost > self.min_cost:
                return

            # Renew when there is a more minimum cost
            elif start == end and self.min_cost > cur_cost:
                self.min_cost_path = []
                self.min_cost_path.append(path)
                self.min_cost = cur_cost

            # Add minimum path
            elif start == end and self.min_cost == cur_cost:
                self.min_cost_path.append(path)

            # Traverse from start to end, recursive
            for row in range(1, N + 1):
                if matrix[start][row] > 0:
                    if row in path:
                        continue
                    dfs(row, path + [row], cur_cost + matrix[start][row])
        dfs(start, [start], 0)
        print(self.min_cost_path)

        #Based on the path of minimum cost, get the result
        def find_res(min_cost_path):
            point_path = []
            res = []

            # Find all traversed node with minimum cost
            for i in min_cost_path:
                for j in range(1, len(i)):
                    point_path.append([i[j], i[j - 1]])
                    point_path.append([i[j - 1], i[j]])
            for i, j, cost in connections:
                if [i, j] in point_path or [j, i] in point_path:
                    res.append('YES')
                else:
                    res.append('NO')
            return res

        return find_res(self.min_cost_path)

if __name__ == '__main__':
    S = Solution()
    test = S.minimumCost(1, 5, 5, [[1,2,1],[2,3,1],[3,4,1],[4,5,1],[5,1,3],[1,3,2],[5,3,1]])
    print(test)
    test = S.minimumCost(1, 4, 4, [[1,2,1],[2,4,1],[1,3,1],[3,4,2],[1,4,2]])
    print(test)
    test = S.minimumCost(1, 5, 5, [[1,2,1],[2,3,1],[3,5,1],[1,4,1],[4,5,2],[3,4,2],[2,4,4]])
    print(test)
    test = S.minimumCost(1, 4, 4, [[1,2,1],[1,3,1],[1,4,1],[2,3,1],[2,4,1]])
    print(test)