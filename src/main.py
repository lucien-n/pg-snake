import sys

from .hud import Hud
from .settings import *
from .fruit import Fruit
from .snake import Snake


class Game:
    def __init__(self) -> None:
        self.size = (settings["display"]["width"], settings["display"]["height"])
        self.window = pg.display.set_mode(
            self.size, display=settings["display"]["display"]
        )
        self.display = pg.Surface(
            (CELL_SIZE * settings["grid"]["size"], CELL_SIZE * settings["grid"]["size"])
        )
        self.clock = pg.time.Clock()

        self.now = 0
        self.dt = 0
        self.prev_time = 0

        self.last_fixed_update_at = 0
        self.fixed_update_rate = 1 / 10

        self.running = True

        self.grid_size = settings["grid"]["size"]

        self.snake = Snake(0, 0, self.grid_size)
        self.fruit = Fruit(self.snake, self.grid_size)
        self.fruit.place()

        self.hud = Hud(self)

    def handle_events(self):
        events = pg.event.get()

        for e in events:
            if e.type == pg.QUIT:
                self.running = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.running = False

        self.snake.handle_events(events)
        self.hud.handle_events(events)

    def update_dt(self):
        self.now = time.time()
        self.dt = self.now - self.prev_time
        self.prev_time = self.now

    def update(self):
        self.update_dt()
        self.fixed_update()

        self.hud.update(self.dt)

    def fixed_update(self):
        if self.now - self.last_fixed_update_at < self.fixed_update_rate:
            return
        self.last_fixed_update_at = self.now

        self.snake.fixed_update(self.dt, self.fruit)

        self.hud.debug("snake.pos", self.snake.parts[-1], "POS")
        self.hud.debug("snake.dir", self.snake.direction, "DIR")
        self.hud.debug("fruit.pos", self.fruit.pos, "FRUIT")

    def draw(self):
        self.window.fill(Color.GRAY)
        self.display.fill(Color.DARK_GRAY)

        self.fruit.draw(self.display)
        self.snake.draw(self.display)

        scaled = pg.transform.scale(self.display, (self.size[1], self.size[1]))
        dest = (m.floor(self.size[0] / 2 - scaled.get_width() / 2), 0)
        self.window.blit(scaled, dest)

        self.hud.draw(self.window)

        pg.display.update()
        self.clock.tick()

    def run(self):
        self.update_dt()
        self.last_fixed_update_at = self.now

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        sys.exit(1)
