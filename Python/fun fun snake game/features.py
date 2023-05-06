# features.py
import random
import pygame

CELL_SIZE = 20
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

class Obstacle:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.position = self.generate()

    def generate(self):
        while True:
            x = random.randrange(0, WIDTH, CELL_SIZE)
            y = random.randrange(0, HEIGHT, CELL_SIZE)
            if (x, y) not in self.snake.body and (x, y) != self.food.position:
                return (x, y)

    def collides_with(self, position):
        return self.position == position

    def out_of_bounds(self):
        return self.position[0] < 0 or self.position[0] >= WIDTH or self.position[1] < 0 or self.position[1] >= HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

class ObstacleManager:
    def __init__(self, snake, board):
        self.snake = snake
        self.board = board
        self.obstacles = []

    def update(self):
        if random.random() < 0.01:
            self.obstacles.append(Obstacle(self.snake, self.board.food)) # Pass snake and food objects here

        self.obstacles = [obstacle for obstacle in self.obstacles if not obstacle.out_of_bounds()]


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def check_collision(self):
        head = self.snake.body[0]
        for obstacle in self.obstacles:
            if obstacle.collides_with(head):  # 使用 collides_with 方法替代 rect.colliderect
                return True
        return False
