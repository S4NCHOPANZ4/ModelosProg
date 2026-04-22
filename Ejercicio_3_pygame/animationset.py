import pygame
from config import Config


# ── Componente base ────────────────────────────────────────────────────────────

class AnimationBase:
    def get(self, direction) -> list:
        raise NotImplementedError


# ── Componente concreto ────────────────────────────────────────────────────────

class Animation(AnimationBase):
    def __init__(self, path):
        self.animations = {
            "down": [],
            "up": [],
            "left": [],
            "right": []
        }

        for i in range(4):
            self.animations["down"].append(
                pygame.image.load(f"{path}/down_{i}.png").convert_alpha()
            )
            self.animations["up"].append(
                pygame.image.load(f"{path}/up_{i}.png").convert_alpha()
            )

        for i in range(2):
            self.animations["left"].append(
                pygame.image.load(f"{path}/left_{i}.png").convert_alpha()
            )
            self.animations["right"].append(
                pygame.image.load(f"{path}/right_{i}.png").convert_alpha()
            )

    def get(self, direction) -> list:
        return self.animations[direction]


# ── Decorador base ─────────────────────────────────────────────────────────────

class AnimationDecorator(AnimationBase):
    def __init__(self, wrapped: AnimationBase):
        self.wrapped = wrapped

    def get(self, direction) -> list:
        return self.wrapped.get(direction)


# ── Decoradores concretos ──────────────────────────────────────────────────────

class ScaleDecorator(AnimationDecorator):
    #Escala todos los frames al tamaño dado.
    def __init__(self, wrapped: AnimationBase, size: tuple = Config.PLAYER_SIZE):
        super().__init__(wrapped)
        self.size = size

    def get(self, direction) -> list:
        frames = self.wrapped.get(direction)
        return [pygame.transform.scale(f, self.size) for f in frames]


class TintDecorator(AnimationDecorator):
    #Aplica un color semitransparente encima de cada frame (util para daño, power-ups, etc.)
    def __init__(self, wrapped: AnimationBase, color: tuple):
        super().__init__(wrapped)
        self.color = color  # (R, G, B, A)

    def get(self, direction) -> list:
        frames = self.wrapped.get(direction)
        tinted = []
        for frame in frames:
            copy = frame.copy()
            overlay = pygame.Surface(copy.get_size(), pygame.SRCALPHA)
            overlay.fill(self.color)
            copy.blit(overlay, (0, 0))
            tinted.append(copy)
        return tinted