import time
import math as m
import pygame as pg
from pygame.math import Vector2 as vector

DEV = True
CELL_SIZE = 32

settings = {
    "display": {"width": 1280, "height": 720, "display": 0},
    "grid": {"size": 24},
}


class Color:
    PINK = (232, 166, 166)
    BEIGE = (165, 114, 95)
    BROWN = (107, 59, 41)
    DARK_RED = (74, 18, 18)
    RED = (177, 44, 28)
    ORANGE = (252, 121, 40)
    YELLOW = (255, 241, 138)
    LIME = (120, 187, 49)
    GREEN = (59, 151, 30)
    DARK_GREEN = (10, 75, 45)
    DARK_BLUE = (67, 122, 160)
    BLUE = (139, 230, 228)
    WHITE = (255, 255, 255)
    GRAY = (134, 139, 156)
    DARK_GRAY = (65, 65, 86)
    BLACK = (0, 0, 0)


class Symbol:
    DELTA = "\u0394"
    EPSYLON = "\u2211"
