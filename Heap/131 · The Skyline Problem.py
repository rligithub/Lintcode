class Solution: # TLE
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        if not buildings:
            return []

        #setup an array to save height
        maxright = float('-inf')
        minleft = float('inf')
        for start, end, h in buildings:
            maxright = max(maxright, end)
            minleft = min(minleft, start)

        table = [0] * (maxright + 1)
        for start, end, h in buildings:
            for i in range(start, end):
                table[i] = max(table[i], h)

        res = []
        left, right = minleft, minleft + 1
        while right < maxright + 1:
            if table[right] == table[left]:
                right += 1
            else:
                if table[left] != 0:
                    res.append([left, right, table[left]])
                left = right

        return res 



