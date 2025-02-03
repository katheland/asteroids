import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0

    # groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        # this lets the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # updates go here
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()

        # render the screen
        screen.fill("black")
        for drawn_thing in drawable:
            drawn_thing.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000

if __name__ == "__main__":
    main()