class Solution:  # valid tree == > no circle
    # check if (x,y) are connected already, if yes, return False; if no, union
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False
        parent = {}
        for i in range(n):
            parent[i] = i
        for i, j in edges:
            found = self.union(parent, i, j)
            if found:
                return False
        return True

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        px, py = self.find(parent, x), self.find(parent, y)
        if px != py:
            parent[px] = py
            return False
        return True




