import pygame
from random import choice
from support import import_folder

# This class handles animations for the game
class AnimationPlayer:
  def __init__(self):
    # Dictionary to store different frames for different animation types
    # The frames are loaded from specified directories

    self.frames = {
			# magic
			'flame': import_folder('./resources/particles/flame/frames'),
			'aura': import_folder('./resources/particles/aura'),
			'heal': import_folder('./resources/particles/heal/frames'),

			# attacks
			'claw': import_folder('./resources/particles/claw'),
			'slash': import_folder('./resources/particles/slash'),
			'sparkle': import_folder('./resources/particles/sparkle'),
			'leaf_attack': import_folder('./resources/particles/leaf_attack'),
			'thunder': import_folder('./resources/particles/thunder'),

			# monster deaths
			'squid': import_folder('./resources/particles/smoke_orange'),
			'raccoon': import_folder('./resources/particles/raccoon'),
			'spirit': import_folder('./resources/particles/nova'),
			'bamboo': import_folder('./resources/particles/bamboo'),

			# leafs
			'leaf': (
				import_folder('./resources/particles/leaf1'),
				import_folder('./resources/particles/leaf2'),
				import_folder('./resources/particles/leaf3'),
				import_folder('./resources/particles/leaf4'),
				import_folder('./resources/particles/leaf5'),
				import_folder('./resources/particles/leaf6'),
				self.reflect_images(import_folder('./resources/particles/leaf1')),
				self.reflect_images(import_folder('./resources/particles/leaf2')),
				self.reflect_images(import_folder('./resources/particles/leaf3')),
				self.reflect_images(import_folder('./resources/particles/leaf4')),
				self.reflect_images(import_folder('./resources/particles/leaf5')),
				self.reflect_images(import_folder('./resources/particles/leaf6'))
				)
			}

  def reflect_images(self, frames):
    # Flip the frames horizontally
    new_frames = []
    for frame in frames:
      flipped_frame = pygame.transform.flip(frame, True, False)
      new_frames.append(flipped_frame)
    return new_frames

  def create_grass_particles(self, pos, groups):
    # Create grass particle effects at a given position
    animation_frames = choice(self.frames['leaf'])
    ParticleEffect(pos, animation_frames, groups)

  def create_particles(self, animation_type, pos, groups):
    # Create a particle effect of a specific type at a given position
    animation_frames = self.frames[animation_type]
    ParticleEffect(pos, animation_frames, groups)

# This class is used to create a particle effect (a type of sprite)
class ParticleEffect(pygame.sprite.Sprite):
  def __init__(self, pos, animation_frames, groups):
    # Initialize the sprite with a position, animation frames, and groups
    super().__init__(groups)
    self.sprite_type = 'magic'
    self.frame_index = 0
    self.animation_speed = 0.15
    self.frames = animation_frames
    self.image = self.frames[self.frame_index]
    self.rect = self.image.get_rect(center = pos)

  def animate(self):
    # Animate the sprite by cycling through its frames
    self.frame_index += self.animation_speed
    if self.frame_index >= len(self.frames):
      self.kill()
    else:
      self.image = self.frames[int(self.frame_index)]

  def update(self):
    # Update the sprite's animation
    self.animate()
