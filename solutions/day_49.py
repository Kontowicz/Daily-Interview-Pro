def inRange(grid, r, c):
    numRow, numCol = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= numRow or c >= numCol:
        return False
    return True

def mark(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    if grid[i][j] != 1:
        return
    grid[i][j] = 2

    mark(grid, i - 1, j)
    mark(grid, i + 1, j)
    mark(grid, i, j - 1)
    mark(grid, i, j + 1)

def numIslands(grid):

    cnt = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 1:
                cnt += 1
                mark(grid, i, j)

    return cnt

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
assert numIslands(grid) == 3