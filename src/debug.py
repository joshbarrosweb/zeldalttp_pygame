import pygame
pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y=10, x=10):
  display_surface = pygame.display.get_surface()

  # Render the debug information as text
  debug_surf = font.render(str(info), True, 'White')

  # Set the position of the debug text
  debug_rect = debug_surf.get_rect(topleft=(x, y))

  # Draw a black rectangle behind the debug text
  pygame.draw.rect(display_surface, 'Black', debug_rect)

  # Blit the debug text onto the display surface
  display_surface.blit(debug_surf, debug_rect)
