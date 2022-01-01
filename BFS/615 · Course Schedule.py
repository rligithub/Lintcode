0import collections


class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # convert prerequisites to neighbors relationship
        # classical topological sort problem
        # set a global variable "count" to see how many courses can be finished
        # if count == numCourses, return True

        neighbors = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)

        for course in range(numCourses):
            indegrees[course] += 0
        for i, j in prerequisites:
            neighbors[j].append(i)
            indegrees[i] += 1

        queue = collections.deque()
        count = 0

        for i in indegrees:
            if indegrees[i] ==0:
                queue.append(i)
        while queue:
            cur = queue.popleft()
            count += 1
            for nei in neighbors[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] ==0:
                    queue.append(nei)
        return count == numCourses


class Solution2:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        neighbor = {i: [] for i in range(numCourses)}

        for i, j in prerequisites:
            neighbor[j].append(i)
            indegree[i] += 1

        queue, count = [], 0
        for index in range(numCourses):
            if indegree[index] == 0:
                queue.append(index)

        while len(queue) > 0:
            course = queue.pop(0)
            count += 1

            for c in neighbor[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)

        return count == numCourses

n = 2
prerequisites = [[1,0],[0,1]]
a= Solution()

print(a.canFinish(n,prerequisites))

