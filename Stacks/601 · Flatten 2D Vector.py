import collections

class Vector2D:

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.queue = collections.deque()
        for row in vec2d:
            self.queue.extend(row)

    # @return {int} a next element
    def next(self):
        if self.hasNext():
            return self.queue.popleft()

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        return self.queue


class Vector2D2:
    def __init__(self, vec2d):
        self.col = 0
        self.row = 0
        self.vec = vec2d

    def next(self):
        if self.hasNext():
            result = self.vec[self.row][self.col]
            self.col += 1
            return result

    def hasNext(self):
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True

            self.col = 0
            self.row += 1

vec2d = [[1,2],[3],[4,5,6]]
a = Vector2D2(vec2d)
while a.hasNext():
    print(a.next())

