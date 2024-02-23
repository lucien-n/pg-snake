from .settings import *
from .fruit import Fruit
from random import randint


class Snake:
    def __init__(self, x: int = 0, y: int = 0, grid_size: int = 32) -> None:
        self.parts = [vector(x, y)]
        self.grid_size = grid_size

        self.direction = vector()

    def handle_events(self, events: list[pg.Event]) -> None:
        for e in events:
            if e.type == pg.KEYDOWN:
                # right
                if e.key == pg.K_d:
                    if self.direction.x == -1:
                        continue
                    self.direction = vector(1, 0)
                # left
                if e.key == pg.K_a:
                    if self.direction.x == 1:
                        continue
                    self.direction = vector(-1, 0)
                # down
                if e.key == pg.K_s:
                    if self.direction.y == -1:
                        continue
                    self.direction = vector(0, 1)
                # up
                if e.key == pg.K_w:
                    if self.direction.y == 1:
                        continue
                    self.direction = vector(0, -1)

    def update(self, dt: float) -> None:
        pass

    def fixed_update(self, dt: float, fruit: Fruit) -> None:
        head = self.parts[-1]
        new_head = head + self.direction

        # out of bounds
        if new_head.x >= self.grid_size:
            new_head.x = 0
        if new_head.x < 0:
            new_head.x = self.grid_size - 1
        if new_head.y >= self.grid_size:
            new_head.y = 0
        if new_head.y < 0:
            new_head.y = self.grid_size - 1

        self.parts.append(new_head)

        if head == fruit.pos:
            fruit.place()
        else:
            self.parts = self.parts[1:]

    def draw(self, target: pg.Surface):
        for part in self.parts:
            part_screen_x, part_screen_y = (
                part.x * CELL_SIZE,
                part.y * CELL_SIZE,
            )
            pg.draw.rect(
                target,
                Color.GREEN,
                pg.Rect(part_screen_x, part_screen_y, CELL_SIZE, CELL_SIZE),
            )
