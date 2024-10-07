import pygame
import random
from consts.consts import Colors, MazeConf


class MazeMap:
    def __init__(self, screen: pygame.Surface) -> None:
        """
        Initialize the MazeMap instance.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.
            screen (pygame.Surface): The Pygame screen to draw the maze.
        """
        self.screen = screen
        self.maze = [
            [0 for _ in range(MazeConf.MAZE_WIDTH)] for _ in range(MazeConf.MAZE_HEIGHT)
        ]
        self.cell_size = self.screen.get_width() // MazeConf.MAZE_WIDTH

    def get_maze(self) -> list[list[int]]:
        """
        Get the current state of the maze.

        Returns:
            list[list[int]]: A 2D list representing the maze.
        """
        return self.maze

    def set_wall(self, x: int, y: int) -> None:
        """
        Set a wall at the specified coordinates.

        Args:
            x (int): The x-coordinate of the wall.
            y (int): The y-coordinate of the wall.
        """
        if self.is_valid_move(x, y):
            self.maze[y][x] = 1

    def is_valid_move(self, x: int, y: int) -> bool:
        """
        Check if a move to the specified coordinates is valid.

        Args:
            x (int): The x-coordinate of the move.
            y (int): The y-coordinate of the move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return 0 <= x < MazeConf.MAZE_WIDTH and 0 <= y < MazeConf.MAZE_HEIGHT

    def set_wall_pattern(self) -> None:
        """
        Set the wall pattern based on the provided maze image.
        """
        wall_coords = [
            (6, 0), (1, 1), (3, 1), (4, 1),
            (6, 1), (8, 1), (9, 1), (1, 2),
            (4, 2), (6, 2), (2, 3), (4, 3),
            (7, 3), (8, 3), (0, 4), (2, 4),
            (4, 4), (5, 4), (8, 4), (2, 5),
            (6, 5), (1, 6), (2, 6), (3, 6),
            (4, 6), (6, 6), (7, 6), (8, 6),
            (9, 6), (4, 7), (6, 7), (0, 8),
            (1, 8), (2, 8), (4, 8), (6, 8),
            (8, 8), (4, 9), (8, 9)

        ]
        for x, y in wall_coords:
            self.set_wall(x, y)

    def draw_maze(self, goal_pos: tuple[int, int]) -> None:
        """
        Draw the maze with the current walls, robot, and goal.

        Args:
            goal_pos (tuple[int, int]): The position of the goal.
            robot_pos (tuple[int, int]): The position of the robot.
        """
        self.screen.fill(Colors.WHITE)

        for i in range(MazeConf.MAZE_WIDTH):
            for j in range(MazeConf.MAZE_HEIGHT):
                x, y = i * self.cell_size, j * self.cell_size
                pygame.draw.rect(
                    self.screen, Colors.GRAY, (x, y, self.cell_size, self.cell_size), 1
                )
                if self.maze[j][i] == 1:
                    pygame.draw.rect(
                        self.screen,
                        Colors.BLACK,
                        (x, y, self.cell_size, self.cell_size),
                    )

        goal_x, goal_y = goal_pos
        pygame.draw.rect(
            self.screen,
            Colors.GREEN,
            (
                goal_x * self.cell_size,
                goal_y * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
        )

        pygame.display.flip()
