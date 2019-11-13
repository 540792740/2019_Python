from heapq import heappush, heappop
import collections

class Solution:

    def checkYourRoute(self, nodes, sources, destinantions, weights, end):
        graph = self.build_graph(nodes, sources, destinantions)
        edge_to_weight = self.get_edge_to_weight(sources, destinantions, weights)
        print('graph',graph)
        print('edge_to_weight', edge_to_weight)
        shortest_dis = self.dijkstra(graph, edge_to_weight)
        print('shortest_dis', shortest_dis)
        results = []
        self.dfs(graph, edge_to_weight, shortest_dis, 0, 1, end, [1], results)
        # for path in results:
        #     print(path)
        return self.formatOutput(results, sources, destinantions)

    def dfs(self, graph, edge_to_weight, shortest_dis, cur_cost, cur, end, path, results):
        if cur == end:
            if cur_cost == shortest_dis[end]:
                print('end', shortest_dis[end])
                results.append(path[:])
            return
        for neighbor in graph[cur]:
            if cur_cost + edge_to_weight[(cur, neighbor)] > shortest_dis[end]:
                continue
            path.append(neighbor)
            next_cost = cur_cost + edge_to_weight[(cur, neighbor)]
            self.dfs(graph, edge_to_weight, shortest_dis, next_cost, neighbor, end, path, results)
            path.pop()
        print('result', results)

    def formatOutput(self, results, sources, destinantions):
        edges_to_index = self.get_edge_to_index(sources, destinantions)
        output = ["NO" for _ in range(len(sources))]
        for path in results:
            for start in range(0, len(path) - 1):
                end = start + 1
                index = edges_to_index[(path[start], path[end])]
                output[index] = "YES"
        return output

    def get_edge_to_index(self, sources, destinantions):
        edges_to_index = {}
        for i in range(len(sources)):
            edges_to_index[(sources[i], destinantions[i])] = i
            edges_to_index[(destinantions[i], sources[i])] = i
        return edges_to_index

    def build_graph(self, nodes, sources, destinantions):
        graph = {node: set() for node in range(1, nodes + 1)}
        for i in range(len(sources)):
            graph[sources[i]].add(destinantions[i])
            graph[destinantions[i]].add(sources[i])
        return graph

    def get_edge_to_weight(self, sources, destinantions, weights):
        edge_to_weight = {}
        for i in range(len(sources)):
            edge_to_weight[(sources[i], destinantions[i])] = weights[i]
            edge_to_weight[(destinantions[i], sources[i])] = weights[i]
        return edge_to_weight

    def dijkstra(self, graph, edge_to_weight):
        d = {i: 2 ** 31 - 1 for i in range(1, len(graph) + 1)}
        print('d', d)
        prev = {i: None for i in range(1, len(graph) + 1)}
        print('prev', prev)
        d[1] = 0
        S = set([1])
        Q = []
        Qd = {}
        for v in graph[1]:
            d[v] = edge_to_weight[(1, v)]             # cost 1 -> v, d[v]
            item = [d[v], 1, v]
            heappush(Q, item)
            Qd[v] = item
        while Q:
            _, parent, u = heappop(Q)
            prev[u] = parent
            if u not in S:
                S.add(u)
                for v in graph[u]:
                    if Qd.get(v):
                        edge = (u, v)
                        if d[v] > d[u] + edge_to_weight[edge]:
                            d[v] = d[u] + edge_to_weight[edge]
                            Qd[v][0] = d[v]
                            Qd[v][1] = u
                            _siftdown(Q, 0, Q.index(Qd[v]))
                    else:
                        d[v] = d[u] + edge_to_weight[(u, v)]
                        item = [d[v], u, v]
                        heappush(Q, item)
                        Qd[v] = item
        return d

if __name__ == '__main__':
    S = Solution()
    sources =       [1, 2, 3, 4, 5, 1, 5]
    destinantions = [2, 3, 4, 5, 1, 3, 3]
    weights =       [1, 1, 1, 1, 3, 2, 1]
    end = 5
    nodes = 5
    output = S.checkYourRoute(nodes, sources, destinantions, weights, end)
    print(output)

class Solution:

    def checkYourRoute(self, nodes, connections, start, end):
        graph, edge_to_weight = self.graph_build(connections)
        shortest_dis = self.dijkstra(graph, edge_to_weight)
        # print(shortest_dis)
        results = []
        self.dfs(graph, edge_to_weight, shortest_dis, 0, 1, end, [1], results)
        for path in results:
            print(path)
        return self.formatOutput(results, sources, destinantions)

    def dfs(self, graph, edge_to_weight, shortest_dis, cur_cost, cur, end, path, results):
        if cur == end:
            if cur_cost == shortest_dis[end]:
                results.append(path[:])
            return
        for neighbor in graph[cur]:
            if cur_cost + edge_to_weight[(cur, neighbor)] > shortest_dis[end]:
                continue
            path.append(neighbor)
            next_cost = cur_cost + edge_to_weight[(cur, neighbor)]
            self.dfs(graph, edge_to_weight, shortest_dis, next_cost, neighbor, end, path, results)
            path.pop()

    def formatOutput(self, results, sources, destinantions):
        edges_to_index = self.get_edge_to_index(sources, destinantions)
        output = ["NO" for _ in range(len(sources))]
        for path in results:
            for start in range(0, len(path) - 1):
                end = start + 1
                index = edges_to_index[(path[start], path[end])]
                output[index] = "YES"
        return output

    def get_edge_to_index(self, sources, destinantions):
        edges_to_index = {}
        for i in range(len(sources)):
            edges_to_index[(sources[i], destinantions[i])] = i
            edges_to_index[(destinantions[i], sources[i])] = i
        return edges_to_index

    def graph_build(self,connections):
        graph = collections.defaultdict(set)
        edge_weight = {}
        for i, j, cost in connections:
            graph[i].add(j)
            graph[j].add(i)
            edge_weight[(i, j)] = cost
            edge_weight[(j, i)] = cost
        return graph, edge_weight

    def dijkstra(self, graph, edge_to_weight):
        d = {i: 2 ** 31 - 1 for i in range(nodes)}
        prev = {i: None for i in range(nodes)}
        d[1] = 0
        S = set([1])
        Q = []
        Qd = {}
        for v in graph[1]:
            d[v] = edge_to_weight[(1, v)]
            item = [d[v], 1, v]
            heappush(Q, item)
            Qd[v] = item
        while Q:
            # print(Q)
            _, parent, u = heappop(Q)
            prev[u] = parent
            if u not in S:
                S.add(u)
                for v in graph[u]:
                    if Qd.get(v):
                        edge = (u, v)
                        if d[v] > d[u] + edge_to_weight[edge]:
                            d[v] = d[u] + edge_to_weight[edge]
                            Qd[v][0] = d[v]
                            Qd[v][1] = u
                            _siftdown(Q, 0, Q.index(Qd[v]))
                    else:
                        d[v] = d[u] + edge_to_weight[(u, v)]
                        item = [d[v], u, v]
                        heappush(Q, item)
                        Qd[v] = item
        return d
# if __name__ == '__main__':
#     S = Solution()
#     nodes = 5
#     start = 1
#     end = 5
#     connections = [[1,2,1],[2,3,1],[3,4,1],[4,5,1],[5,1,3],[1,3,2],[5,3,1]]
#     test = S.checkYourRoute(nodes, connections, start, end)
#     print(output)
