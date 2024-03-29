from .settings import *
from .fruit import Fruit
from random import randint


class Snake:
    def __init__(
        self, x: int = 0, y: int = 0, grid_size: int = 32, color: Color = Color.LIME
    ) -> None:
        self.parts = [vector(x, y)]
        self.grid_size = grid_size
        self.color = color

        self.direction = vector()
        self.old_direction = vector()

        self.head_sprite = pg.transform.scale(
            pg.image.load("assets/sprites/snake_head.png").convert_alpha(),
            (CELL_SIZE, CELL_SIZE),
        )
        self.body_sprite = pg.transform.scale(
            pg.image.load("assets/sprites/snake_body.png").convert_alpha(),
            (CELL_SIZE, CELL_SIZE),
        )

    def handle_events(self, events: list[pg.Event]) -> None:
        for e in events:
            if e.type == pg.KEYDOWN:
                # right
                if e.key == pg.K_d:
                    if self.old_direction.x == -1:
                        continue
                    self.direction = vector(1, 0)
                # left
                if e.key == pg.K_a:
                    if self.old_direction.x == 1:
                        continue
                    self.direction = vector(-1, 0)
                # down
                if e.key == pg.K_s:
                    if self.old_direction.y == -1:
                        continue
                    self.direction = vector(0, 1)
                # up
                if e.key == pg.K_w:
                    if self.old_direction.y == 1:
                        continue
                    self.direction = vector(0, -1)

    def update(self, dt: float) -> None:
        pass

    def fixed_update(self, dt: float, fruit: Fruit) -> None:
        self.old_direction = self.direction

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
        for i, part in enumerate(self.parts):
            x, y = (
                part.x * CELL_SIZE,
                part.y * CELL_SIZE,
            )

            if i == len(self.parts) - 1:
                angle = 0
                if self.direction.x == 1:
                    angle = 270
                if self.direction.x == -1:
                    angle = 90
                if self.direction.y == 1:
                    angle = 180

                target.blit(pg.transform.rotate(self.head_sprite, angle), (x, y))
            else:
                target.blit(self.body_sprite, (x, y))
