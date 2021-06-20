import collections


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        if not node:
            return None

        queue = collections.deque()
        queue.append(node)

        visited = set()
        visited.add(node)

        while queue:
            cur = queue.popleft()
            if values[cur] == target:
                return cur
            for i in cur.neighbors:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

        return None


