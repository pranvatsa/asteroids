# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main() -> None:
    """Main game loop for Asteroids."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set containers for automatic group management
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    score = 0
    font = pygame.font.SysFont(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()  # Only shoot on key press

        updatable.update(dt)

        # Player-asteroid collision
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

        # Bullet-asteroid collision
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 100

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        # Draw score
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()