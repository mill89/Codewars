def maze_runner(maze: list, directions: list) -> str:
    # lost dead finish
    # 0 = Безопасное место для прогулок
    # 1 = Стена
    # 2 = Начальная точка
    # 3 = точка финиша
    l = len(maze) - 1
    start = finish = ()
    wall = []

    for x, row in enumerate(maze):
        for y, num in enumerate(row):
            if num == 1:
                wall.append((x, y))
            elif num == 2:
                start = (x, y)
            elif num == 3:
                finish = (x, y)

    # N: -x, S: +x, W: -y, E: +y
    runner = start
    for x in directions:
        if runner in wall:
            break
        elif x == 'N':
            runner = (runner[0] - 1, runner[1])
        elif x == 'S':
            runner = (runner[0] + 1, runner[1])
        elif x == 'W':
            runner = (runner[0], runner[1] - 1)
        elif x == 'E':
            runner = (runner[0], runner[1] + 1)

    if runner == finish:
        return f'Finish - {runner}'
    elif runner in wall or runner[0] > l or runner[0] < 0 or runner[1] > l or runner[1] < 0:
        return f'Dead - {runner}'
    else:
        return f'Lost - {runner}'


if __name__ == '__main__':
    maze = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 3],
            [1, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 2, 1, 0, 1, 0, 1]]

    print(maze_runner(maze, ["N", "E", "E", "S", "S", "S"]))

    # assert maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]) == "Finish"
    # assert maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "E", "E", "N", "N", "E"]) == "Finish"
    # assert maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E", "W", "W"]) == "Lost"
    # assert maze_runner(maze, ["N", "N", "N", "W", "W"]) == "Dead"
    # assert maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"]) == "Dead"
    # assert maze_runner(maze, ["N", "E", "E", "E", "E"]) == "Lost"

    print(maze_runner(maze, ["N", "E", "E", "E", "E"]))
