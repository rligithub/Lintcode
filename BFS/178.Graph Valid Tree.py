import collections


class Solution:
    def validTree(self, n: int, edges) -> bool:
        if not n:
            return True

        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        return self.dfs(graph, 0, -1, visited) and n == len(visited)

    def dfs(self, graph, node, parent, visited):
        if node in visited:
            return False

        visited.add(node)
        for nei in graph[node]:
            if nei == parent:
                continue
            if not self.dfs(graph, nei, node, visited):
                return False

        return True


class Solution4:
    def validTree(self, n, edges):
        if n== 0 or n ==1:
            return True
        if n != len(edges) + 1:
            return False
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque()
        queue.append(edges[0][0])
        visited = set()

        while queue:
            cur = queue.popleft()
            for i in graph.get(cur,[]):
                if i in visited:
                    continue
                queue.append(i)
                visited.add(i)
        return len(visited) == n





n = 5
edges = [[4,1],[4,2],[4,3],[0,4]]
a = Solution()

print(a.validTree(n, edges))


