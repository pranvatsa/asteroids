import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Shot(CircleShape):
    """A bullet fired by the player."""

    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """Draw the shot as a yellow circle."""
        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            2
        )

    def update(self, dt: float):
        """Move the shot and wrap around the screen."""
        self.position += self.velocity * dt
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT