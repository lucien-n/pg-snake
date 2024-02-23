from .settings import *
from random import randint


class Fruit:

    def __init__(self, snake, grid_size: int = 32) -> None:
        from .snake import Snake

        self.pos = vector()
        self.snake: Snake = snake
        self.grid_size = grid_size

    def place(self):
        self.pos = vector(
            randint(0, self.grid_size - 1), randint(0, self.grid_size - 1)
        )
        if self.pos in self.snake.parts:
            self.place()

    def draw(self, target: pg.Surface):
        fruit_screen_x, fruit_screen_y = (
            self.pos.x * CELL_SIZE,
            self.pos.y * CELL_SIZE,
        )

        pg.draw.rect(
            target,
            Color.RED,
            pg.Rect(fruit_screen_x, fruit_screen_y, CELL_SIZE, CELL_SIZE),
        )