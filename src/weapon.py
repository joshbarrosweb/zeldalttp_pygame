import pygame

# Create a class for the Weapon, inheriting from the Sprite class in Pygame.
class Weapon(pygame.sprite.Sprite):
  def __init__(self, player, groups):
    # Initialize the Sprite class
    super().__init__(groups)
    # Define the type of sprite
    self.sprite_type = 'weapon'
    # Extract the direction from the player status
    direction = player.status.split('_')[0]

    # Construct the full path to the image file based on player's weapon and direction
    full_path = f'./resources/weapons/{player.weapon}/{direction}.png'
    # Load the image and convert the pixel format for better performance
    self.image = pygame.image.load(full_path).convert_alpha()

    # Set the position of the weapon relative to the player based on the direction.
    # The weapon will appear to the right of the player when the player is facing right.
    if direction == 'right':
      self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0, 16))
    # The weapon will appear to the left of the player when the player is facing left.
    elif direction == 'left':
      self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0, 16))
    # The weapon will appear below the player when the player is facing down.
    elif direction == 'down':
      self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10, 0))
    # The weapon will appear above the player when the player is facing up.
    elif direction == 'up':
      self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(10, 0))
    # If no valid direction is found, the weapon will appear in the center of the player.
    else:
      self.rect = self.image.get_rect(center = player.rect.center)
