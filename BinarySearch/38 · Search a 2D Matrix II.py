print('38 · Search a 2D Matrix II')
def searchMatrix(self, matrix, target):
    if not matrix or not matrix[0]:
        return 0

    m,n = len(matrix),len(matrix[0])
    x,y = 0, n-1
    count=0
    while x<=m-1 and y>=0:
        goal=matrix[x][y]
    # search from the right upper corner (max value in row 0, min value in column n)
    # if target > goal, move to next row x++
    # if target < goal, move to previous column y--
    # if target == goal, count ++, move to next row x++ and previous column y--
        if target > goal:
            x +=1
        if target < goal:
            y -=1
        if target == goal:
            count +=1
            y -=1
            x +=1
    return count

matrix = [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]

target = 7

print(searchMatrix(0,matrix,target))
