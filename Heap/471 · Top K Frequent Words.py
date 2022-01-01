import heapq
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        heap = []
        table = collections.defaultdict(int)
        res = []
        for word in words:
            if table[word]:
                table[word] +=1
            else:
                table[word] = 1
        for key in table:
            heapq.heappush(heap, (- table[key],key))
        for i in range(min(len(words), k)):
            value, key = heapq.heappop(heap)
            res.append(key)
        return res
