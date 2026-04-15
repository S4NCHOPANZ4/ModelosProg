import pygame

class Animation:
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

    def get(self, direction):
        return self.animations[direction]