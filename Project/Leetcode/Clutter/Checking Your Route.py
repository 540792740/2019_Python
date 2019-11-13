
class Solution(object):

    def minimumCost(self, start, end, N, connections):
        matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for i, j, cost in connections:
            matrix[i][j] = cost
            matrix[j][i] = cost
        self.min_cost = 2**31 - 1
        self.res = []
        def dfs(start, path, cur_cost):
            # print(path, cur_cost)
            if cur_cost > self.min_cost:
                return
            elif start == end and self.min_cost > cur_cost:
                self.res = []
                self.res.append(path)
                self.min_cost = cur_cost
            elif start == end and self.min_cost == cur_cost:
                self.res.append(path)
            for row in range(1, N + 1):
                if matrix[start][row] > 0:
                    if row in path:
                        continue
                    dfs(row, path + [row], cur_cost + matrix[start][row])
        dfs(start, [start], 0)

        def find_res(res):
            point_path = []
            res_value = []
            for i in res:
                for j in range(1, len(i)):
                    print(i)
                    point_path.append([i[j], i[j - 1]])
                    point_path.append([i[j - 1], i[j]])
            print(point_path)
            for i, j, cost in connections:
                print([i, j])
                if [i, j] in point_path or [j, i] in point_path:
                    res_value.append('YES')
                else:
                    res_value.append('NO')
            return res_value
        return find_res(self.res)

if __name__ == '__main__':
    S = Solution()
    test = S.minimumCost(1, 5, 5, [[1,2,1],[2,3,1],[3,4,1],[4,5,1],[5,1,3],[1,3,2],[5,3,1]])
    test = S.minimumCost(1, 4, 4, [[1,2,1],[2,4,1],[1,3,1],[3,4,2],[1,4,2]])
    test = S.minimumCost(1, 5, 5, [[1,2,1],[2,3,1],[3,5,1],[1,4,1],[4,5,2],[3,4,2],[2,4,4]])
    test = S.minimumCost(1, 4, 4, [[1,2,1],[1,3,1],[1,4,1],[2,3,1],[2,4,1]])
    print(test)