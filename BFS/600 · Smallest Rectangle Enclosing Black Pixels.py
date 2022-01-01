import collections


class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # to find the rectangle to cover all "1", need to find "1" in leftest, righest, top and bottom
        # calculate the areas

        m,n = len(image), len(image[0])
        queue = collections.deque()
        queue.append((x,y))
        minX, maxX, maxY,minY= x,x,y,y
        visited = set()
        visited.add((x,y))
        while queue:
            i,j = queue.popleft()
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                xx, yy = i + dx, j + dy
                if 0<= xx < m and 0<= yy < n and image[xx][yy] == 1 and (xx,yy) not in visited:
                    queue.append((xx,yy))
                    visited.add((xx,yy))
                    minX=min(minX,xx)
                    maxX=max(maxX,xx)
                    minY=min(minY,yy)
                    maxY=max(maxY,yy)

        return (maxX-minX+1)*(maxY-minY+1)


from collections import deque


class Solution2:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """

    def minArea(self, image, x, y):
        # write your code here
        n, m = len(image), len(image[0])
        ## binary search
        top = self.binary_search(image, 0, x)
        bottom = self.binary_search(image, n - 1, x)
        left = self.binary_search(image, 0, y, is_row=False)
        right = self.binary_search(image, m - 1, y, is_row=False)

        return (bottom - top + 1) * (right - left + 1)

    def binary_search(self, image, start, end, is_row=True):

        n = (len(image) - 1) if is_row else (len(image[0]) - 1)
        if start > end:
            s, e = n - start, n - end
        else:
            s, e = start, end

        while s + 1 < e:
            mid = (s + e) // 2

            if start > end:
                mid_p = n - mid
            else:
                mid_p = mid

            if is_row:
                arr = [int(r) for r in image[mid_p]]
            else:
                arr = [int(r[mid_p]) for r in image]

            if sum(arr) > 0:
                e = mid
            else:
                s = mid

        if start > end:
            s = n - s
            e = n - e

        if is_row:
            arr_s = [int(r) for r in image[s]]
        else:
            arr_s = [int(r[s]) for r in image]

        if sum(arr_s) == 0:
            return e
        else:
            return s

image = [[0,0,1,0],
         [0,1,1,0],
         [0,1,0,0]]
x = 0
y = 2

a = Solution()
print(a.minArea(image,x,y))