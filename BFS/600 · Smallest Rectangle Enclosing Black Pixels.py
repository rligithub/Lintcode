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


image = [[0,0,1,0],
         [0,1,1,0],
         [0,1,0,0]]
x = 0
y = 2

a = Solution()
print(a.minArea(image,x,y))