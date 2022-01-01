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
        visited = set()
        for course in org:
            indegrees[course] += 0
        for s in seqs:
            visited |= set(s)
            for i in range(len(s) - 1):
                if s[i] not in indegrees or s[i+1] not in indegrees:
                    return False
                neighbors[s[i]].append(s[i+1])
                indegrees[s[i+1]] += 1

        queue = collections.deque()
        res = []
        for i in indegrees:
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            if len(queue) > 1:
                return False
            cur = queue.popleft()
            res.append(cur)
            for nei in neighbors[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return res == org and len(visited) == len(org)




org = []
seqs = [[]]


a= Solution()
print(a.sequenceReconstruction(org,seqs))