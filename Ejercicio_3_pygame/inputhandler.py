import pygame
from vector2 import Vector2



class InputHandler:
    def get_direction(self):
        keys = pygame.key.get_pressed()

        direction = Vector2()

        if keys[pygame.K_w]:
            direction.y = -1
        if keys[pygame.K_s]:
            direction.y = 1
        if keys[pygame.K_a]:
            direction.x = -1
        if keys[pygame.K_d]:
            direction.x = 1

        if direction.x == 0 and direction.y == 0:
            return None

        direction.normalize()
        return direction