def maze_runner(maze, directions):
    n = len(maze)

    # find start point
    for i in range(n):
        if 2 in maze[i]:
            row = i
            col = maze[row].index(2)
            break

    # follow directions
    for step in directions:
        if step == "N":
            row -= 1
        elif step == "S":
            row += 1
        elif step == "E":
            col += 1
        elif step == "W":
            col -= 1

        # check the result
        if row < 0 or col < 0 or row == n or col == n or maze[row][col] == 1:
            return "Dead"
        elif maze[row][col] == 3:
            return "Finish"

    return "Lost"


# DIRS = {'S': (1,0), 'E': (0,1), 'N': (-1,0), 'W': (0,-1)}
#
# def maze_runner(maze, directions):
#     maze = [l + [1] for l in maze] + [[1] * len(maze[0])]
#     y, x = next((y,x) for y, l in enumerate(maze) for x, c in enumerate(l) if c == 2)
#     for dy, dx in map(DIRS.get, directions):
#         y += dy; x += dx
#         if maze[y][x] == 3: return 'Finish'
#         if maze[y][x] == 1: return 'Dead'
#     return 'Lost'