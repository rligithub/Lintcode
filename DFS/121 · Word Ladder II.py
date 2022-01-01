import collections
import string


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        # step1: find all valid words in dict for "end" word
        # step2: use bfs to create a graph for distances of all valid words to "end" word
        # step3: use dfs to for loop all word in graph and find the previous valid word for "start" word, print out path

        dict.append(start)
        dict.append(end)

        queue = collections.deque()
        queue.append(end)       #use bfs find the distances of all valid words to "end" word
        distances = collections.defaultdict(int)
        distances[end] = 0

        while queue:
            cur = queue.popleft()
            for word in self.validWord(cur, dict):
                if word not in distances:
                    distances[word] = distances[cur] + 1
                    queue.append(word)

        res = []
        self.dfs(start, end, dict, distances, [start], res)
        return res

    def validWord(self, word, dict):
        ans = []
        str = string.ascii_lowercase
        for i in range(len(word)):
            for char in str:
                matchedWord = word[:i] + char + word[i+1:]
                if matchedWord in dict:
                    ans.append(matchedWord)
        return ans

    def dfs(self, cur, target, dict, distances, path, res):
        if cur == target:
            return res.append(path)

        for word in self.validWord(cur, dict):
            if distances[word] != distances[cur] -1:
                continue
            self.dfs(word, target, dict, distances, path + [word], res)



import string

class Solution2:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # step1: find all valid words in dict for "end" word
        # step2: use bfs to create a graph for distances of all valid words to "end" word
        # step3: use dfs to for loop all word in graph and find the previous valid word for "start" word, print out path

        dict.add(start)
        dict.add(end)

        self.table = collections.defaultdict(list)

        queue = collections.deque()
        queue.append(end)       #use bfs find the distances of all valid words to "end" word
        distances = collections.defaultdict(int)
        distances[end] = 0

        while queue:
            cur = queue.popleft()
            for word in self.validWord(cur, dict):
                if word not in distances:
                    distances[word] = distances[cur] + 1
                    queue.append(word)

        res = []
        self.dfs(start, end, dict, distances, [start], res)
        return res

    def validWord(self, word, dict):
        res = []
        str = string.ascii_lowercase
        for i in range(len(word)):
            for char in str:
                matchedWord = word[:i] + char + word[i+1:]
                if matchedWord in dict:
                    res.append(matchedWord)
        self.table[word].extend(res)
        return res

    def dfs(self, cur, target, dict, distances, path, res):
        if cur == target:
            return res.append(path)

        # for word in self.validWord(cur, dict):
        for word in self.table[cur]:
            if distances[word] != distances[cur] - 1:
                continue
            self.dfs(word, target, dict, distances, path + [word], res)


start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]

a = Solution()
print(a.findLadders(start, end, dict))