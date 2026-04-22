import pygame
import sys
from config import Config
from player import Player
from inputhandler import InputHandler
from animationset import Animation

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Movimiento continuo")

        self.clock = pygame.time.Clock()
        self.player = Player(200, 100)
        self.input_handler = InputHandler()

        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(Config.FPS) / 1000  # segundos

            self.handle_events()
            self.update(dt)
            self.render()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        direction = self.input_handler.get_direction()
        self.player.update(direction, dt)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        pygame.display.flip()

