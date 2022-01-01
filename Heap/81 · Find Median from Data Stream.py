import heapq


class Solution: # time complexity is too long
    def __init__(self):
        self.heap = []

    """
    @param val: An integer
    @return: nothing
    """

    def add(self, val):
        heapq.heappush(self.heap, val)

    """
    @return: return the median of the data stream
    """

    def getMedian(self):
        res = []
        mid = (len(self.heap) - 1) // 2
        for i in range(mid + 1):
            res.append(heapq.heappop(self.heap))
        for num in res:
            heapq.heappush(self.heap, num)
        return res[-1]

class Solution2:
    #use two heap
    #轮流存在heap1 和heap2里，median在长度小的那个heap里

    def __init__(self):
        self.maxheap =[]
        self.minheap =[]

    """
    @param val: An integer
    @return: nothing
    """
    def add(self, val):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -val)
        else:
            heapq.heappush(self.minheap, val)
        if len(self.maxheap) ==0 or len(self.minheap) == 0:
            return

        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))
            heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))


    """
    @return: return the median of the data stream
    """
    def getMedian(self):
        return -self.maxheap[0]

class Solution3: # easy version
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