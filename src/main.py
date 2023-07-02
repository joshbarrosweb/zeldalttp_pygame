import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda PYTHON')
        self.clock = pygame.time.Clock()

        self.level = Level()  # Initialize game level

        # Load and play main background sound
        main_sound = pygame.mixer.Sound('./resources/audio/main.ogg')
        main_sound.set_volume(0.6)
        main_sound.play(loops = -1)

    def run(self):
        # Main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()  # Toggle menu on/off

            # Draw the background
            self.screen.fill(WATER_COLOR)

            # Update the level
            self.level.run()

            # Refresh the display
            pygame.display.update()
            self.clock.tick(FPS)  # Cap the frame rate

if __name__ == '__main__':
    game = Game()
    game.run()
