import collections


class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        queue = collections.deque()

        if not nodes:
            return []

        level, res = [],[]
        visited = set()
        for node in nodes:
            if node in visited:
                continue

            queue.append(node)
            visited.add(node)
            level =[]
            while queue:
                cur = queue.popleft()
                level.append(cur.label)
                for nei in cur.neighbors:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            level.sort()
            res.append(level)
        return res







