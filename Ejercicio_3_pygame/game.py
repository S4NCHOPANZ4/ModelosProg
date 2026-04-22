import pygame
import sys
from config import Config
from player import Player
from inputhandler import InputHandler
from tile import TileMap


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Movimiento continuo")

        self.clock = pygame.time.Clock()
        self.player = Player(200, 100)
        self.input_handler = InputHandler()
        self.tilemap = TileMap(tile_size=80)

        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(Config.FPS) / 1000

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

        # Centro del player para detectar la tile
        cx = self.player.x + Config.PLAYER_SIZE[0] / 2
        cy = self.player.y + Config.PLAYER_SIZE[1] / 2
        tile = self.tilemap.get_tile_at(cx, cy)

        tile_type = tile.tile_type if tile else "grass"
        self.player.apply_tile_effect(tile_type)

    def render(self):
        self.screen.fill((60, 60, 60))  # fondo oscuro para tiles sin cubrir
        self.tilemap.draw(self.screen)
        self.player.draw(self.screen)
        self._draw_hud()
        pygame.display.flip()

    def _draw_hud(self):
        tile_type = self.player._current_tile_type or "grass"
        labels = {
            "grass": ("GRASS", (80, 200, 80)),
            "water": ("WATER", (80, 140, 255)),
            "lava":  ("LAVA",  (255, 80, 20)),
        }
        text, color = labels.get(tile_type, ("?", (255, 255, 255)))
        font = pygame.font.SysFont(None, 28)
        surf = font.render(f"Tile: {text}", True, color)
        self.screen.blit(surf, (10, 10))
