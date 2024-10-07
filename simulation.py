import pygame
from consts.consts import MazeConf
from environment.map import MazeMap


pygame.init()
screen = pygame.display.set_mode((MazeConf.SCREEN_WIDTH, MazeConf.SCREEN_HEIGHT))

maze_map = MazeMap(screen)
maze_map.set_wall_pattern()

goal_pos_x, goal_pos_y = MazeConf.GOAL_X, MazeConf.GOAL_Y
maze_map.draw_maze((goal_pos_x, goal_pos_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
