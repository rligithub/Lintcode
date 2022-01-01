
import heapq
import collections

heap = 0
nums = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5]]


table = collections.defaultdict(list)

for id, score in nums:
    heapq.heappush(table[id], score)

print(heap)
print(heap)






