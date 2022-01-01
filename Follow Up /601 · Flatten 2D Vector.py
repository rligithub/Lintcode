import collections


class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.queue = collections.deque()
        for item in vec2d:
            self.queue.extend(item)

    # @return {int} a next element
    def next(self):
        if self.hasNext:
            return self.queue.popleft()

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        return self.queue

    # Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())