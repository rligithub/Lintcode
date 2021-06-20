import collections


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # create neighbors relationship
        # classical topological sort problems
        # create global variable "count" for finished courses
        # if numCourses = count, return res = order of finished courses; if numCourses != count, return []

        neighbors = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for course in range(numCourses):
            indegrees[course] += 0

        for u,v in prerequisites:
            neighbors[v].append(u)
            indegrees[u] += 1

        queue = collections.deque()
        count = 0
        res = []
        for i in indegrees:
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            count +=1
            res.append(cur)
            for nei in neighbors[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)

        if count == numCourses:
            return res
        else:
            return []

