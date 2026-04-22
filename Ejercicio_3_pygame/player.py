import pygame
from config import Config
from animationset import Animation, ScaleDecorator, TintDecorator
from state import IdleState, MoveState


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.animation = ScaleDecorator(
            Animation("assets/player")
        )
        # Ejemplo con tint encima:
        # self.animation = TintDecorator(
        #     ScaleDecorator(Animation("assets/player")),
        #     color=(255, 0, 0, 80)
        # )

        self.direction = "down"
        self.frame = 0
        self.timer = 0

        self.speed = Config.PLAYER_SPEED

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
        self.x %= Config.WIDTH
        self.y %= Config.HEIGHT

    def draw(self, screen):
        frames = self.animation.get(self.direction)
        self.frame = self.frame % len(frames)
        frame = frames[self.frame]

        w, h = frame.get_size()

        x_offsets = [0]
        if self.x < w:
            x_offsets.append(Config.WIDTH)
        elif self.x > Config.WIDTH - w:
            x_offsets.append(-Config.WIDTH)

        y_offsets = [0]
        if self.y < h:
            y_offsets.append(Config.HEIGHT)
        elif self.y > Config.HEIGHT - h:
            y_offsets.append(-Config.HEIGHT)

        for ox in x_offsets:
            for oy in y_offsets:
                screen.blit(frame, (self.x + ox, self.y + oy))