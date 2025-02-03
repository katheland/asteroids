import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init(self, x, y, radius):
        super().__init(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    # when an asteroid is killed, spawn new ones if it was big enough
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        new_size = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_size)
        new_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_size)
        new_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2