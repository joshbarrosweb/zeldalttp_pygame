import pygame
from settings import *
from support import *
from tile import Tile
from player import Player
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade

# The main Level class
class Level:
  def __init__(self):
    # Get the current display surface
    self.display_surface = pygame.display.get_surface()

    # Flag to check if game is paused
    self.game_paused = False

    # Create different types of sprite groups
    self.visible_sprites = YSortCameraGroup()
    self.obstacle_sprites = pygame.sprite.Group()
    self.attack_sprites = pygame.sprite.Group()
    self.attackable_sprites = pygame.sprite.Group()

    # Reference to the current attack (weapon)
    self.current_attack = None

    # Create the initial game map
    self.create_map()

    # Create the UI and the upgrade system
    self.ui = UI()
    self.upgrade = Upgrade(self.player)

    # Initialize animation and magic systems
    self.animation_player = AnimationPlayer()
    self.magic_player = MagicPlayer(self.animation_player)

  def create_map(self):
    # Create a map by importing different tile layouts from CSV files
    # and importing graphics from the resources folders

    layouts = {
      'boundary': import_csv_layout('./resources/map/map_FloorBlocks.csv'),
      'grass': import_csv_layout('./resources/map/map_Grass.csv'),
      'object': import_csv_layout('./resources/map/map_LargeObjects.csv'),
      'entities': import_csv_layout('./resources/map/map_Entities.csv')
    }
    graphics = {
      'grass': import_folder('./resources/grass'),
      'objects': import_folder('./resources/objects')
    }

    for style, layout in layouts.items():

      for row_index, row in enumerate(layout):
        for col_index, col in enumerate(row):
          if col != '-1':
            x = col_index * TILESIZE
            y = row_index * TILESIZE
            if style == "boundary":
              Tile((x, y), [self.obstacle_sprites], 'invisible')

            if style == 'grass':
              random_grass_image = choice(graphics['grass'])
              Tile(
                (x, y),
                [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites],
                'grass',
                random_grass_image
              )

            if style == 'object':
              surf = graphics['objects'][int(col)]
              Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

            if style == 'entities':
              if col == '394':
                self.player = Player(
                  (x, y),
                  [self.visible_sprites],
                  self.obstacle_sprites,
                  self.create_attack,
                  self.destroy_attack,
                  self.create_magic
                )
              else:
                if col == '390': monster_name = 'bamboo'
                elif col == '391': monster_name = 'spirit'
                elif col == '392': monster_name = 'raccoon'
                else: monster_name = 'squid'

                Enemy(
                  monster_name,
                  (x, y),
                  [self.visible_sprites, self.attackable_sprites],
                  self.obstacle_sprites,
                  self.damage_player,
                  self.trigger_death_particles,
                  self.add_exp
                )


  def create_attack(self):
    # Create a new weapon instance

    self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

  def destroy_attack(self):
    # Destroy the current weapon instance

    if self.current_attack:
      self.current_attack.kill()
    self.current_attack = None

  def player_attack_logic(self):
    # Implement the logic for the player's attack

    if self.attack_sprites:
      for attack_sprite in self.attack_sprites:
        collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
        if collision_sprites:
          for target_sprite in collision_sprites:
            if target_sprite.sprite_type == 'grass':
              pos = target_sprite.rect.center
              offset = pygame.math.Vector2(0, 75)
              for leaf in range(randint(3, 6)):
                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
              target_sprite.kill()
            else:
              target_sprite.get_damage(self.player, attack_sprite.sprite_type)

  def damage_player(self, amount, attack_type):
    # Damage the player by a given amount and type of attack

    if self.player.vulnerable:
      self.player.health -= amount
      self.player.vulnerable = False
      self.player.hurt_time = pygame.time.get_ticks()

      self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

  def trigger_death_particles(self, pos, particle_type):
    # Trigger death particles at a given position and of a specific type

    self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

  def create_magic(self, style, strength, cost):
    # Create a magic effect of a given style, strength, and cost

    if style == 'heal':
      self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])

    if style == 'flame':
      self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

  def add_exp(self, amount):
    # Add a given amount of experience to the player

    self.player.exp += amount

  def toggle_menu(self):
    # Toggle the game menu on and off

    self.game_paused = not self.game_paused

  def run(self):
    # Main run loop for the level

    self.visible_sprites.custom_draw(self.player)
    self.ui.display(self.player)

    if self.game_paused:
      self.upgrade.display()
    else:
      self.visible_sprites.update()
      self.visible_sprites.enemy_update(self.player)
      self.player_attack_logic()

# A sprite group that sorts sprites by their Y coordinate and updates
# enemy sprites based on the player's position
class YSortCameraGroup(pygame.sprite.Group):
  def __init__(self):
    # Initialize the sprite group and load the floor surface

    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.half_width = self.display_surface.get_size()[0] // 2
    self.half_height = self.display_surface.get_size()[1] // 2
    self.offset = pygame.math.Vector2()

    self.floor_surf = pygame.image.load('./resources/tilemap/ground.png').convert()
    self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))

  def custom_draw(self, player):
    # Draw the sprites onto the display surface, sorted by their Y coordinate

    self.offset.x = player.rect.centerx - self.half_width
    self.offset.y = player.rect.centery - self.half_height

    floor_offset_pos = self.floor_rect.topleft - self.offset
    self.display_surface.blit(self.floor_surf, floor_offset_pos)

    for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
      offset_pos = sprite.rect.topleft - self.offset
      self.display_surface.blit(sprite.image, offset_pos)

  def enemy_update(self, player):
    # Update the state of enemy sprites based on the player's position

    enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
    for enemy in enemy_sprites:
      enemy.enemy_update(player)
