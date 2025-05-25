import pygame

class CircleShape(pygame.sprite.Sprite):
    """Base class for circular game objects."""

    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Override in subclasses to draw the object."""
        pass

    def update(self, dt: float):
        """Override in subclasses to update the object."""
        pass

    def collides_with(self, other: "CircleShape") -> bool:
        """Returns True if this circle collides with another circle."""
        return self.position.distance_to(other.position) < (self.radius + other.radius)