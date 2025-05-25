import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED,
    PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
)
from shot import Shot

class Player(CircleShape):
    """Player spaceship controlled by the user."""

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0

    def triangle(self):
        """Return the three points of the player's triangle for drawing."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draw the player as a white triangle."""
        pygame.draw.polygon(
            screen,
            (255, 255, 255),
            [point for point in self.triangle()],
            2
        )

    def rotate(self, dt: float):
        """Rotate the player by turn speed and delta time."""
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float):
        """Move the player forward in the direction it is facing."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        """Shoot a bullet if cooldown allows."""
        if self.shoot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt: float):
        """Update player state, handle input and cooldowns."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        # No shooting here; handled in main.py KEYDOWN event
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            if self.shoot_timer < 0:
                self.shoot_timer = 0