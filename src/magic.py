import pygame
from random import randint
from settings import *

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        # Load sounds
        self.sounds = {
            'heal': pygame.mixer.Sound('./resources/audio/heal.wav'),
            'flame': pygame.mixer.Sound('./resources/audio/flame.wav'),
        }

    def heal(self, player, strength, cost, groups):
        # Perform a heal on the player
        if player.energy >= cost:
            self.sounds['heal'].play()  # Play healing sound
            player.health += strength  # Increase player's health
            player.energy -= cost  # Decrease player's energy

            if player.health >= player.stats['health']:
                player.health = player.stats['health']

            # Create healing animations
            self.animation_player.create_particles('aura', player.rect.center,  groups)
            self.animation_player.create_particles('heal', player.rect.center + pygame.math.Vector2(0, -60),  groups)

    def flame(self, player, cost, groups):
        # Perform a flame attack
        if player.energy >= cost:
            player.energy -= cost  # Decrease player's energy
            self.sounds['flame'].play()  # Play flame sound

        # Determine the direction of the flame based on the player's status
        if player.status.split('_')[0] == 'right':
          direction = pygame.math.Vector2(1, 0)
        elif player.status.split('_')[0] == 'left':
          direction = pygame.math.Vector2(-1, 0)
        elif player.status.split('_')[0] == 'up':
          direction = pygame.math.Vector2(0, -1)
        else:
          direction = pygame.math.Vector2(0, 1)

        # Create flame animations
        for i in range(1, 6):
          if direction.x:
            offset_x = (direction.x * i) * TILESIZE
            x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
            y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
            self.animation_player.create_particles('flame', (x, y), groups)
          else:
            offset_y = (direction.y * i) * TILESIZE
            x = player.rect.centerx  + randint(-TILESIZE // 3, TILESIZE // 3)
            y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
            self.animation_player.create_particles('flame', (x, y), groups)
