with open("input.txt") as f:
    grid = [list(row.strip()) for row in f]

H = len(grid)
W = len(grid[0])

dirs = [(-1,-1), (-1,0), (-1,1),
        ( 0,-1),         ( 0,1),
        ( 1,-1), ( 1,0), ( 1,1)]

counter = 0

for i in range(H):
    for j in range(W):
        at = 0

        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if grid[i][j] != ".":
                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == "@":
                    at += 1

        if grid[i][j] != "." and at < 4:
            counter += 1

print(counter)