import pygame
from config import Config
from animationset import Animation, ScaleDecorator, TintDecorator
from state import IdleState, MoveState


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Animación base (sin decoradores extra)
        self._base_animation = ScaleDecorator(Animation("assets/player"))
        self.animation = self._base_animation

        self.direction = "down"
        self.frame = 0
        self.timer = 0

        self.speed = Config.PLAYER_SPEED

        self.states = {
            "idle": IdleState(),
            "move": MoveState()
        }
        self.state = self.states["idle"]

        # Tile actual bajo el player (para no re-aplicar el decorador cada frame)
        self._current_tile_type = None

    def change_state(self, new_state):
        self.state = self.states[new_state]
        self.frame = 0
        self.timer = 0

    def apply_tile_effect(self, tile_type: str | None):
        """Aplica o quita un TintDecorator según la tile bajo el player."""
        if tile_type == self._current_tile_type:
            return  # nada cambió, no hacemos nada

        self._current_tile_type = tile_type

        if tile_type == "lava":
            self.animation = TintDecorator(self._base_animation, color=(255, 60, 0, 120))
        elif tile_type == "water":
            self.animation = TintDecorator(self._base_animation, color=(0, 100, 255, 90))
        else:
            # grass u otro: animación limpia
            self.animation = self._base_animation

    def update(self, direction, dt):
        self.state.update(self, dt, direction)
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
