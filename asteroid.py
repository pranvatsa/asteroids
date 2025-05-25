import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid(CircleShape):
    """Asteroid object that can split into smaller asteroids."""

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw the asteroid as a light gray circle."""
        pygame.draw.circle(
            screen,
            (200, 200, 200),
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            2
        )

    def update(self, dt: float):
        """Move the asteroid and wrap around the screen."""
        self.position += self.velocity * dt
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def split(self):
        """Split the asteroid into two smaller asteroids, or destroy if at minimum size."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2