import pygame
from settings import *

# The UI class manages all aspects of the game's user interface
class UI:
  # The constructor for the UI class
  def __init__(self):
    self.display_surface = pygame.display.get_surface() # Obtain the display surface for rendering UI components
    self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE) # Initialize the font for UI text

    # Create rectangles for health and energy bars with appropriate dimensions
    self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
    self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

    # Load weapon graphics for the weapon overlay
    self.weapon_graphics = []
    for weapon in weapon_data.values():
      path = weapon['graphic']
      weapon = pygame.image.load(path).convert_alpha()
      self.weapon_graphics.append(weapon)

    # Load magic graphics for the magic overlay
    self.magic_graphics = []
    for magic in magic_data.values():
      path = magic['graphic']
      magic = pygame.image.load(path).convert_alpha()
      self.magic_graphics.append(magic)

  # Method to render a bar (e.g. health, energy) on the screen
  def show_bar(self, current, max_amount, bg_rect, color):
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

    # Calculate the width of the current value bar
    ratio = current / max_amount
    current_width = bg_rect.width * ratio
    current_rect = bg_rect.copy()
    current_rect.width = current_width

    # Draw the current value bar and border
    pygame.draw.rect(self.display_surface, color, current_rect)
    pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

  # Method to render experience on the screen
  def show_exp(self, exp):
    text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
    x = self.display_surface.get_size()[0] - 20
    y = self.display_surface.get_size()[1] - 20
    text_rect = text_surf.get_rect(bottomright = (x, y))

    pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
    self.display_surface.blit(text_surf, text_rect)

  # Method to render a selection box for weapons or magic
  def selection_box(self, left, top, has_switched):
    bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
    if has_switched:
      pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
    else:
      pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
    return bg_rect

  # Method to render the weapon overlay
  def weapon_overlay(self, weapon_index, has_switched):
    bg_rect = self.selection_box(10, 630, has_switched)
    weapon_surf = self.weapon_graphics[weapon_index]
    weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

    self.display_surface.blit(weapon_surf, weapon_rect)

  # Method to render the magic overlay
  def magic_overlay(self, magic_index, has_switched):
    bg_rect = self.selection_box(80, 630, has_switched)
    magic_surf = self.magic_graphics[magic_index]
    magic_rect = magic_surf.get_rect(center = bg_rect.center)

    self.display_surface.blit(magic_surf, magic_rect)

  # Method to display the entire UI
  def display(self, player):
    self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
    self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)

    self.show_exp(player.exp)

    self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
    self.magic_overlay(player.magic_index, not player.can_switch_magic)
