from config import Config
from vector2 import Vector2
from animationset import Animation
import pygame

from animationset import Animation
from state import IdleState, MoveState

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.animation = Animation("assets/player")

        self.direction = "down"
        self.frame = 0
        self.timer = 0

        self.speed = 200

        # State Pattern
        self.states = {
            "idle": IdleState(),
            "move": MoveState()
        }

        self.state = self.states["idle"]

    def change_state(self, new_state):
        self.state = self.states[new_state]
        self.frame = 0
        self.timer = 0

    def update(self, direction, dt):
        self.state.update(self, dt, direction)

        # tp
        from config import Config
        self.x %= Config.WIDTH
        self.y %= Config.HEIGHT

    def draw(self, screen):
        frames = self.animation.get(self.direction)
        self.frame = self.frame % len(frames)
        frame = frames[self.frame]
        screen.blit(frame, (self.x, self.y))