import collections


class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution1:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
    # record the values for in-degree of each nodes
    # when in-degree == 0, we can delete the nodes
    # res = [order of deleted nodes]
        if not graph:
            return []

        indegrees = collections.defaultdict(int)
        for i in graph:
            indegrees[i] += 0
            for j in i.neighbors:
                indegrees[j] += 1  # to record numbers of neighbors for each node

        queue = collections.deque()
        for i in indegrees:
            if indegrees[i] == 0:
                queue.append(i)     # add initial node into the queue (indegree ==0)

        res = []

        while queue:
            cur = queue.popleft()
            res.append(cur)
            for j in cur.neighbors:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    queue.append(j)

        return res


"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""



class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here

        # BFS
        from collections import defaultdict
        indegrees = defaultdict(int)

        queue = []
        result = []

        # construct the indegrees
        for node in graph:
            curr_neighbor = node.neighbors
            indegrees[node] += 0
            for end in curr_neighbor:
                indegrees[end] += 1

        # initialize the queue with 0-indegree nodes
        for node in indegrees.keys():
            if indegrees[node] == 0:
                queue.append(node)

        # typical BFS
        while len(queue):
            current_node = queue.pop()
            result.append(current_node)
            for end in current_node.neighbors:
                indegrees[end] -= 1
                if indegrees[end] == 0:
                    queue.append(end)

        return result