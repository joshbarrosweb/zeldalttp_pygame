import pygame
from settings import *

# Define a class for Tile objects which extends pygame's sprite class
class Tile(pygame.sprite.Sprite):
  # The constructor for the Tile class
  def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
    super().__init__(groups) # Call the parent constructor, passing the groups to the superclass's constructor

    self.sprite_type = sprite_type # Set the sprite_type of the tile
    y_offset = HITBOX_OFFSET[sprite_type] # Retrieve y-offset for the given sprite type from global constants

    self.image = surface # Set the surface image of the tile

    # If the sprite type is 'object', adjust the rect of the tile to accommodate the object's position
    if sprite_type == 'object':
      self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - TILESIZE))
    else:
      self.rect = self.image.get_rect(topleft = pos) # If not 'object', the rect is set to the given position directly

    # The hitbox of the tile is set to be an inflated version of the rect by the y-offset amount
    self.hitbox = self.rect.inflate(0, y_offset)
