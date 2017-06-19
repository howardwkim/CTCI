
def paint_fill(canvas, row, col, new_color):
    prev_color = canvas[row][col]
    height = len(canvas)
    width = len(canvas)
    canvas[row][col] = new_color
    q = [[row,col]]

    while q:
        current_pixel = q.pop(0)
        r,c = current_pixel[0], current_pixel[1]

        if r - 1 >= 0:
            if canvas[r-1][c] == prev_color:
                canvas[r-1][c] = new_color
                q.append([r - 1, c])
        if r + 1 < height:
            if canvas[r+1][c] == prev_color:
                canvas[r+1][c] = new_color
                q.append([r + 1, c])
        if c - 1 >= 0:
            if canvas[r][c-1] == prev_color:
                canvas[r][c-1] = new_color
                q.append([r, c - 1])
        if c + 1 < width:
            if canvas[r][c+1] == prev_color:
                canvas[r][c+1] = new_color
                q.append([r, c + 1])

    return canvas


test = [[0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0]]

for row in paint_fill(test, 2,2,3):
    print row
print

test = [[0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0]]
for row in paint_fill(test, 3,4,3):
    print row
print

test = [[0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0]]
for row in paint_fill(test, 4, 4, 3):
    print row
print


'''
did not check for whether paint is within bound of canvas
if point in canvas == new_color, nothing will happen, but my code still runs. Still okay, but should mention.
Need better naming to shorten amount of writing if possible

'''