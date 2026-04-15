
class State:
    def update(self, player, dt, direction):
        pass


class IdleState(State):
    def update(self, player, dt, direction):
        if direction:
            player.change_state("move")


class MoveState(State):
    def update(self, player, dt, direction):
        if not direction:
            player.change_state("idle")
            return

        # Movimiento
        player.x += direction.x * player.speed * dt
        player.y += direction.y * player.speed * dt

        # Dirección lógica
        if abs(direction.x) > abs(direction.y):
            player.direction = "right" if direction.x > 0 else "left"
        else:
            player.direction = "down" if direction.y > 0 else "up"

        # Animación
        frames = player.animation.get(player.direction)

        player.timer += dt
        if player.timer > 0.15:
            player.frame = (player.frame + 1) % len(frames)
            player.timer = 0