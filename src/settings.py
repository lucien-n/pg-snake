import time
import math as m
import pygame as pg
from pygame.math import Vector2 as vector

DEV = True
CELL_SIZE = 32

settings = {
    "display": {"width": 1280, "height": 720, "display": 0},
    "grid": {"size": 32},
}


class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
