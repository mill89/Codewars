def maze_runner(maze, directions):
    # Find the starting position
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 2:
                start_row, start_col = i, j

    # Define the directions
    moves = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

    # Initialize the current position
    current_row, current_col = start_row, start_col

    # Follow the directions
    for direction in directions:
        move = moves[direction]
        current_row += move[0]
        current_col += move[1]

        # Check if the new position is within the maze boundaries
        if current_row < 0 or current_row >= len(maze) or current_col < 0 or current_col >= len(maze[0]):
            return "Dead"  # Hit the maze border

        # Check if the new position is a wall
        if maze[current_row][current_col] == 1:
            return "Dead"  # Hit a wall

        # Check if the new position is the finish point
        if maze[current_row][current_col] == 3:
            return "Finish"

    # Check if the player is still in the maze after using all moves
    if 0 <= current_row < len(maze) and 0 <= current_col < len(maze[0]):
        return "Lost"


# Example usage:
maze = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 3],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 2, 1, 0, 1, 0, 1]]

directions = ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]

result = maze_runner(maze, directions)
print(result)
