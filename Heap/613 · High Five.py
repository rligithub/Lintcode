
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

import collections
import heapq

class Solution1:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        hashmap = collections.defaultdict(list)

        for id, score in results:
            heapq.heappush(hashmap[id], score)
            if len(hashmap[id]) > 5:
                heapq.heappop(hashmap[id], score)

        avgscore = collections.defaultdict(int)
        for id in hashmap:
            avgscore[id] = sum(hashmap[id]) / len(hashmap[id])

        return avgscore


class Solution2:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        hashmap = dict()
        avgscore = dict()

        for result in results:
            if result.id not in hashmap:
                hashmap[result.id] = []
            heapq.heappush(hashmap[result.id], result.score)
            if len(hashmap[result.id]) > 5:
                heapq.heappop(hashmap[result.id])

            avgscore[result.id] = sum(hashmap[result.id]) / len(hashmap[result.id])
        return avgscore


results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60]]

a = Solution1()
print(a.highFive(results))







