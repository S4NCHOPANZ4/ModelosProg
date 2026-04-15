class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def normalize(self):
        mag = (self.x**2 + self.y**2) ** 0.5
        if mag > 0:
            self.x /= mag
            self.y /= mag
