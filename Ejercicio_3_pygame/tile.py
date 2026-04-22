import pygame


TILE_COLORS = {
    "grass": (100, 180, 80),
    "water": (60, 120, 220),
    "lava":  (220, 60, 10),
}


class Tile:
    def __init__(self, col, row, tile_type: str, tile_size: int):
        self.tile_type = tile_type
        self.rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)

    def draw(self, screen):
        color = TILE_COLORS.get(self.tile_type, (80, 80, 80))
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)  # borde


class TileMap:
    # Layout: 0=grass, 1=water, 2=lava
    LAYOUT = [
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 2, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    TYPE_MAP = {0: "grass", 1: "water", 2: "lava"}

    def __init__(self, tile_size: int = 80):
        self.tile_size = tile_size
        self.tiles: list[Tile] = []

        for row, cols in enumerate(self.LAYOUT):
            for col, val in enumerate(cols):
                self.tiles.append(Tile(col, row, self.TYPE_MAP[val], tile_size))

    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

    def get_tile_at(self, px: float, py: float) -> Tile | None:
        """Devuelve la tile bajo el centro del player."""
        for tile in self.tiles:
            if tile.rect.collidepoint(px, py):
                return tile
        return None
