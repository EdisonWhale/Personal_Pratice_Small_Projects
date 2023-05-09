# fun fun snake Game

This repository contains a classic Snake game implemented in Python using the Pygame library. The game features a snake that grows in size as it eats food, and obstacles that the snake must avoid. The game ends when the snake collides with itself, the screen edges, or an obstacle. The goal is to achieve the highest score possible.

![snake game](https://user-images.githubusercontent.com/103423072/236656068-7b8e97e5-ec57-4bf4-bcff-eb62a0246c00.gif)

## Features

- Snake grows in size as it eats food
- Obstacles appear randomly on the board
- Snake speed increases as its size grows
- Game over when the snake collides with itself, screen edges, or an obstacle
- Displays score and speed on the screen

## Prerequisites

To run the game, you need to have Python and Pygame installed on your system. You can install Pygame using the following command:

```
pip install pygame
```

## Running the game

To run the game, navigate to the repository directory and execute the following command:

```
python main.py
```


## Controls

- Up Arrow: Move the snake up
- Down Arrow: Move the snake down
- Left Arrow: Move the snake left
- Right Arrow: Move the snake right

When the game is over, you can click the buttons on the screen:

- Click "Restart" to restart the game
- Click "Quit" to quit the game

## Code Structure

The code is divided into two files:

1. `main.py`: Contains the main game loop and classes for the game, including the `Game`, `Snake`, `Food`, and `Board` classes.
2. `features.py`: Contains the `Obstacle` and `ObstacleManager` classes that handle obstacle generation and management.

## Acknowledgements

This project uses the [Pygame](https://www.pygame.org/) library for game development.
