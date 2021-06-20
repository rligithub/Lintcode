import collections


class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # step1: copy initial nodes
        # step2: find all nodes, copy nodes
        # step3: copy edges

        if not node:
            return None

        queue = collections.deque()
        queue.append(node)
        visited = {}
        visited[node] = UndirectedGraphNode(node.label) # copy initial nodes

        while queue:
            cur = queue.popleft()

            for i in cur.neighbors:
                if i not in visited:
                    visited[i] = UndirectedGraphNode(i.label)   # copy all nodes
                    queue.append(i)
                visited[cur].neighbors.append(visited[i])       # copy all edges and relationship 
        return node

