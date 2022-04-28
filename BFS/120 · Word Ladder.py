import collections


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        if not dict or not start or not end:course
            return -1
        if start == end:
            return 1

        queue = collections.deque()
        queue.append(start)
        count =1
        visited = set()
        visited.add(start)
        dict.append(start)
        dict.append(end)
        while queue:
            count += 1
            size = len(queue)
            for x in range(size):
                cur = queue.popleft()
                for word in self.validWord(cur,dict):
                    if word in visited:
                        continue
                    if word == end:
                        return count
                    queue.append(word)
                    visited.add(word)

        return 0

    def validWord(self,word,dict):
        res = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                matchWord = left + char + right
                if matchWord in dict:
                    res.append(matchWord)
        return res


class Solution2:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):

        if start == end:
            return 1
        ans = 1
        q = [start]
        abc = 'abcdefghijklmnopqrstuvwxyz'
        while q:
            ans += 1
            size = len(q)
            for _ in range(size):
                temp = list(q.pop(0))
                for i in range(len(temp)):
                    ch = temp[i]
                    for j in range(26):
                        temp[i] = abc[j]
                        new_word = ''.join(temp)
                        if new_word == end:
                            return ans
                        if new_word in dict:
                            q.append(new_word)
                            dict.remove(new_word)
                    temp[i] = ch
        return 0

class Solution3: #double queue
    def ladderLength(self, start, end, dict):
        if start == end:
            return 1

        ans = 1
        q1 = {start}
        q2 = {end}
        abc = 'abcdefghijklmnopqrstuvwxyz'
        while q1 and q2:
            ans += 1
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            new_q = set()
            for word in q1:
                temp = list(word)
                for i in range(len(temp)):
                    ch = temp[i]
                    for j in range(26):
                        temp[i] = abc[j]
                        new_word = ''.join(temp)
                        if new_word in q2:
                            return ans
                        if new_word in dict:
                            new_q.add(new_word)
                            dict.remove(new_word)
                    temp[i] = ch
            q1 = new_q
        return -1



start ="abc"
end = "xbf"
dict =["hot","abf","dog","lot"]

a = Solution()
print(a.ladderLength(start, end, dict))