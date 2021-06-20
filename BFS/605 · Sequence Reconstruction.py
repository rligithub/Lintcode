import collections


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        if not org:
            return True
        if not seqs or not any(seqs):
            return False

        neighbors = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)

        for course in org:
            indegrees[course] += 0
        for i, j in seqs:
            neighbors[i].append(j)
            indegrees[j] += 1

        queue = collections.deque()

        for i in indegrees:
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            if len(queue) > 1:
                return False
            cur = queue.popleft()
            for nei in neighbors[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)




org = []
seqs = [[]]


a= Solution()
print(a.sequenceReconstruction(org,seqs))