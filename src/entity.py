import pygame
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()  # Set initial direction

    def move(self, speed):
        # Move entity in the current direction at a given speed
        if self.direction.magnitude() != 0:  # If entity has a direction
            self.direction = self.direction.normalize()  # Normalize direction vector

            # Move horizontally
            self.hitbox.x += self.direction.x * speed
            self.collision("horizontal")

            # Move vertically
            self.hitbox.y += self.direction.y * speed
            self.collision("vertical")

            # Update sprite's position
            self.rect.center = self.hitbox.center

    def collision(self, direction):
        # Check for collision with any obstacle sprite
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # If collision occurred, adjust position
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # If collision occurred, adjust position
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def wave_value(self):
        # Get a waving value for some effects
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0
