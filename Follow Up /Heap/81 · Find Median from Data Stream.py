import heapq
class Solution:
    # median ==> smaller number in mid
    def __init__(self):
        self.maxheap =[]
        self.minheap =[]

    def add(self, val):
        # push val to maxheap
        # move largest val to minheap -- > minheap always larger num
        # determine if len(minheap) > len(maxheap) --> maxheap always more num, smaller num
        # midian == maxheap[0]

        heapq.heappush(self.minheap, - heapq.heappushpop(self.maxheap,- val))
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def getMedian(self):
        return -self.maxheap[0]
