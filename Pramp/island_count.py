direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def getNumberOfIslands(binaryMatrix):
    island_count = 0

    for row in range(len(binaryMatrix)):
        for col in range(len(binaryMatrix[0])):
            if col == 1:
                islandSearch(row, col, binaryMatrix)
                island_count += 1
    return island_count


def islandSearch(row, col, binaryMatrix):
    if binaryMatrix[row][col] == 0 or binaryMatrix[row][col] == -1:
        return
    if binaryMatrix[row][col] == 1:
        binaryMatrix[row][col] = -1

    row_length_max = len(binaryMatrix) - 1
    col_length_max = len(binaryMatrix[0]) - 1

    direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for dir in direction:
        x, y = row + dir[0], col + dir[1]
        if x > 0 and x <= row_length_max and y > 0 and y <= col_length_max:
            islandSearch(x, y, binaryMatrix)

    if row + 1 <= row_length_max:
        islandSearch(row + 1, col, binaryMatrix)
    if row - 1 >= 0:
        islandSearch(row - 1, col, binaryMatrix)
    if col + 1 <= col_length_max:
        islandSearch(row, col + 1, binaryMatrix)
    if col - 1 >= 0:
        islandSearch(row, col - 1, binaryMatrix)


BinaryMatrix = [[0, 1, 0, 1, 0],
                [0, 0, 1, 1, 1],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [1, 0, 1, 0, 1]]

print getNumberOfIslands(BinaryMatrix)
# output: 6 # since this is the


# 0<= idRow <= len(binaryMatrix) - 1
# 0<= idCol <= len(binaryMatrix[0]) - 1
# row+1, col
# row-1, col
# row, col+1
# row, col-1


# iterate through binaryMatrix
# if we encounter a 1 - islandSearch
# mark the first one, then search for adjacent ones
# islandSearch on the adjacent ones
# increment islandCounter


for i in range(0,0):
    print i