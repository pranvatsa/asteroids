# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Create a Clock object
    dt = 0  # Delta time variable

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  # New group for shots

    # Set containers for Player, Asteroid, Shot
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)  # Add this line

    # Create player and asteroid field after setting containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)  # Update all updatables

        # Collision detection: check if player collides with any asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

        screen.fill((0, 0, 0))  # Fill the screen with black
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()   # Refresh the display

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds

if __name__ == "__main__":
    main()