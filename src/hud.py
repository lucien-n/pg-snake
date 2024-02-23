import numpy as np
from .settings import *
import pygame.freetype as pgft


class Hud:
    pgft.init()

    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game

        self.font = pgft.Font(r"assets/fonts/default.ttf", 12, False, False)

        self.last_update_at = 0
        self.update_interval = 1 / 10

        self.debug_lines = {}
        self.rendered_lines = []

        self.show_debug = False

        self.fps_list = []

    def handle_events(self, events: list[pg.Event]):
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_F3:
                    self.show_debug = not self.show_debug

    def update(self, dt: float):
        if self.game.now - self.last_update_at < self.update_interval:
            return
        self.last_update_at = self.game.now

        self.debug("dt", f"{(dt * 1_000):.2f}", Symbol.DELTA, "ms", Color.ORANGE)

        self.fps_list.append(m.floor(self.game.clock.get_fps()))
        self.fps_list = self.fps_list[-30:]

        self.debug("fps", m.floor(np.mean(self.fps_list)), Symbol.EPSYLON, bg=Color.RED)

        self.redraw()

    def redraw(self):
        self.rendered_lines.clear()
        for rendered_line in self.debug_lines.values():
            rendered_line = self.render_font(
                f'{rendered_line["label"]} {rendered_line["value"]}{rendered_line.get("unit", "")}',
                20,
                rendered_line.get("fg_color", (255, 255, 255)),
                rendered_line.get("bg_color", (253, 187, 109)),
                5,
            )
            self.rendered_lines.append(rendered_line)

    def draw(self, surface: pg.Surface, *args):
        if self.show_debug:
            h = 0
            for rendered_line in self.rendered_lines:
                surface.blit(rendered_line, (0, h))
                h += rendered_line.get_height()

    def debug(
        self,
        key: str,
        value: any,
        label: Symbol | str,
        unit: str = "",
        bg: Color = Color.DARK_BLUE,
        fg: Color = Color.WHITE,
    ):
        self.debug_lines[key] = {
            "label": str(label),
            "value": str(value),
            "unit": str(unit),
            "bg_color": bg,
            "fg_color": fg,
        }

    def render_font(
        self,
        content: str = "Placeholder",
        size: int = 20,
        color: tuple = (255, 255, 255),
        bgcolor: tuple = None,
        padding: int = 4,
    ) -> pg.Surface:
        """Render text with font

        Args:
            content (str, optional): Rendered text. Defaults to "Placeholder".
            size (int, optional): Font size. Defaults to 20.
            color (tuple, optional): Font color. Defaults to (255, 255, 255).
            bgcolor (tuple, optional): Background color. Defaults to None.
            padding (int, optional): Padding. Defaults to 4.

        Returns:
            pygame.Surface: Rendered text surface
        """
        rendered_text = self.font.render(
            str(content), color, None, pgft.STYLE_DEFAULT, 0, size
        )[0]

        padded_rendered_text = pg.Surface(
            (
                rendered_text.get_width() + padding * 2,
                rendered_text.get_height() + padding * 2,
            )
        )
        padded_rendered_text.convert_alpha()

        if bgcolor:
            padded_rendered_text.fill(bgcolor)

        padded_rendered_text.blit(rendered_text, (padding, padding))

        return padded_rendered_text
