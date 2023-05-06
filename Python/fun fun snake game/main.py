import pygame
import sys
import random
import time
from features import Obstacle, ObstacleManager

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.food = Food(self.snake)
        self.board = Board(self.snake, self.food)
        self.obstacle_manager = ObstacleManager(self.snake, self.board)
        self.font = pygame.font.Font(None, 24)

    def run(self):
        while True:
            running = self.game_loop()
            if not running:
                break

    def game_loop(self):
        while True:
            self.handle_events()  # This line should be here
            self.snake.move()

            if self.board.check_game_state() or self.obstacle_manager.check_collision():
                self.show_game_over()
                if not self.handle_game_over():
                    return False

            self.board.update()
            self.obstacle_manager.update()

            self.draw()
            self.clock.tick(self.snake.speed)
        return True
    
    def handle_events(self):  # Move this function inside the Game class
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)


    # New methods
    def show_game_over(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)

        font_small = pygame.font.Font(None, 24)
        text = font_small.render("Press 'R' to restart or 'Q' to quit", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        self.screen.blit(text, text_rect)

        pygame.display.flip()

    def handle_game_over(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.quit_button.collidepoint(x, y):
                        return False
                    elif self.restart_button.collidepoint(x, y):
                        self.snake = Snake()
                        self.food = Food(self.snake)
                        self.board = Board(self.snake, self.food)
                        return True
                elif event.type == pygame.QUIT:
                    return False
            self.clock.tick(30)  # Add this line to fix the issue with restart button

    def draw(self):
        self.screen.fill(WHITE)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.board.draw_obstacles(self.screen)  # Add this line to draw the obstacles
        self.show_score()
        pygame.display.flip()

    def show_game_over(self):
        font_big = pygame.font.Font(None, 48)
        game_over_text = font_big.render("Game Over", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        self.screen.blit(game_over_text, game_over_rect)

        quit_text = self.font.render("Quit", True, BLACK)
        self.quit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 80, 40)
        pygame.draw.rect(self.screen, RED, self.quit_button)
        self.screen.blit(quit_text, self.quit_button.move(20, 10))

        restart_text = self.font.render("Restart", True, BLACK)
        self.restart_button = pygame.Rect(WIDTH // 2 + 20, HEIGHT // 2, 80, 40)
        pygame.draw.rect(self.screen, GREEN, self.restart_button)
        self.screen.blit(restart_text, self.restart_button.move(5, 10))

        pygame.display.flip()

    def show_score(self):
        score_text = self.font.render(f"Score: {self.snake.score}", True, GREEN)
        speed_text = self.font.render(f"Speed: {round(self.snake.speed)}", True, GREEN)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(speed_text, (WIDTH - 100, 10))



class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (CELL_SIZE, 0)
        self.score = 0
        self.speed = 6

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])
        self.score += 1
        self.speed += 0.2

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != (0, CELL_SIZE):
            self.direction = (0, -CELL_SIZE)
        elif key == pygame.K_DOWN and self.direction != (0, -CELL_SIZE):
            self.direction = (0, CELL_SIZE)
        elif key == pygame.K_LEFT and self.direction != (CELL_SIZE, 0):
            self.direction = (-CELL_SIZE, 0)
        elif key == pygame.K_RIGHT and self.direction != (-CELL_SIZE, 0):
            self.direction = (CELL_SIZE, 0)

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake):
        self.snake = snake
        self.position = self.generate()

    def generate(self):
        while True:
            x = random.randrange(0, WIDTH, CELL_SIZE)
            y = random.randrange(0, HEIGHT, CELL_SIZE)
            if (x, y) not in self.snake.body:
                return (x, y)

    def is_eaten(self):
        return self.snake.body[0] == self.position

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

class Board:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.obstacles = [Obstacle(self.snake, self.food) for _ in range(10)]  # Add 10 obstacles


    def update(self):
        if self.food.is_eaten():
            self.snake.grow()
            self.food.position = self.food.generate()

    def check_game_state(self):
        head = self.snake.body[0]
        if head in self.snake.body[1:] or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or any(head == obstacle.position for obstacle in self.obstacles):  # Check if the snake head collides with any obstacle
            return True
        return False

    def draw_obstacles(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def is_snake_on_food(self):
        return self.snake.body[0] == self.food.position

class Food:
    def __init__(self, snake):
        self.snake = snake
        self.position = self.generate()

    def generate(self):
        while True:
            x = random.randrange(0, WIDTH, CELL_SIZE)
            y = random.randrange(0, HEIGHT, CELL_SIZE)
            if (x, y) not in self.snake.body:
                return (x, y)

    def is_eaten(self):
        return self.snake.body[0] == self.position

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

if __name__ == "__main__":
    game = Game()
    game.run()