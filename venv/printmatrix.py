class solution():
    counter = 0
    def sprialprint(self, matrix, offset, size):
        if size <= 1:
            print(self.counter+1)
            return

        for i in range(size - 1):
            matrix[0 + offset][i + offset] = self.counter
            self.counter +=1
            print(self.counter)
        for i in range(size - 1):
            matrix[i + offset][size - offset-1] = self.counter
            self.counter +=1
            print(self.counter)

        for i in range(size - 1):
            matrix[size - 1 -offset][size-i - 1-offset] = self.counter
            self.counter += 1
            print(self.counter)


        for i in range(size - 1):
            matrix[size-i-1-offset][0 + offset] = self.counter
            self.counter += 1
            print(self.counter)


        self.sprialprint(matrix, offset + 1, size - 2)

a = solution()

matrix = [[1,2,3,4,5],
          [16,17,18,19,6],
          [15,24,25,20,7],
          [14,23,22,21,8],
          [13,12,11,10,9]
          ]



matrix2 = [[1,2,3,4,5,6,7],
           [24,25,26,27,28,29,8],
           [23,40,41,42,43,30,9],
           [22,39,48,49,44,31,10],
           [21,38,47,46,45,32,11],
           [20,37,36,35,34,33,12],
           [19,18,17,16,15,14,13]
           ]


print(a.sprialprint(matrix,0,5))

