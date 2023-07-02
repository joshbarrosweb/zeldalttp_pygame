import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
  def __init__(self, monster_name, pos, groups, obstacle_sprites, damage_player, trigger_death_particles, add_exp):
    # Constructor of the Enemy class

    super().__init__(groups) # Initialize parent Entity class
    self.sprite_type = 'enemy'

    # Load graphics and set the initial state
    self.import_graphics(monster_name)
    self.status = 'idle'
    self.image = self.animations[self.status][self.frame_index]

    # Set position and collision
    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)
    self.obstacle_sprites = obstacle_sprites

    # Initialize monster-specific attributes
    self.monster_name = monster_name
    monster_info = monster_data[self.monster_name]
    self.health = monster_info['health']
    self.exp = monster_info['exp']
    self.speed = monster_info['speed']
    self.attack_damage = monster_info['damage']
    self.resistance = monster_info['resistance']
    self.attack_radius = monster_info['attack_radius']
    self.notice_radius = monster_info['notice_radius']
    self.attack_type = monster_info['attack_type']

    # Initialize attack properties
    self.can_attack = True
    self.attack_time = None
    self.attack_cooldown = 400
    self.damage_player = damage_player
    self.trigger_death_particles = trigger_death_particles
    self.add_exp = add_exp

    # Initialize vulnerability properties
    self.vulnerable = True
    self.hit_time = None
    self.invincibility_duration = 300

    # Initialize sounds and set volumes
    self.death_sound = pygame.mixer.Sound('./resources/audio/death.wav')
    self.hit_sound = pygame.mixer.Sound('./resources/audio/hit.wav')
    self.attack_sound = pygame.mixer.Sound(monster_info['attack_sound'])
    self.death_sound.set_volume(0.2)
    self.hit_sound.set_volume(0.2)
    self.attack_sound.set_volume(0.3)

  def import_graphics(self, name):
    # Import animations for idle, move, and attack states
    self.animations = {'idle': [], 'move': [], 'attack': []}
    main_path = f'./resources/monsters/{name}/'
    for animation in self.animations.keys():
      self.animations[animation] = import_folder(main_path + animation)

  def get_player_distance_direction(self, player):
    # Calculate the distance and direction between enemy and player
    enemy_vec = pygame.math.Vector2(self.rect.center)
    player_vec = pygame.math.Vector2(player.rect.center)
    distance = (player_vec - enemy_vec).magnitude()

    # Return a normalized direction vector if distance is not zero, otherwise return zero vector
    if distance > 0:
      direction = (player_vec - enemy_vec).normalize()
    else:
      direction = pygame.math.Vector2()

    return (distance, direction)

  def get_status(self, player):
    # Determine the status (idle, move, attack) based on player distance
    distance = self.get_player_distance_direction(player)[0]

    # Change status based on distance and ability to attack
    if distance <= self.attack_radius and self.can_attack:
      if self.status != 'attack':
        self.frame_index = 0
      self.status = 'attack'
    elif distance <= self.notice_radius:
      self.status = 'move'
    else:
      self.status = 'idle'

  def actions(self, player):
    # Perform actions based on the current status
    if self.status == 'attack':
      self.attack_time = pygame.time.get_ticks()
      self.damage_player(self.attack_damage, self.attack_type)
      self.attack_sound.play()
    elif self.status == 'move':
      self.direction = self.get_player_distance_direction(player)[1]
    else:
      self.direction = pygame.math.Vector2()

  def animate(self):
    # Animate the enemy based on the current status
    animation = self.animations[self.status]
    self.frame_index += self.animation_speed

    # Reset animation index after reaching the end, and disable attacking after attack animation
    if self.frame_index >= len(animation):
      if self.status == 'attack':
        self.can_attack = False
      self.frame_index = 0

    self.image = animation[int(self.frame_index)]
    self.rect = self.image.get_rect(center=self.hitbox.center)

    # Set the transparency based on vulnerability
    if not self.vulnerable:
      alpha = self.wave_value()
      self.image.set_alpha(alpha)
    else:
      self.image.set_alpha(255)

  def cooldown(self):
    # Apply cooldown for attack and vulnerability
    current_time = pygame.time.get_ticks()
    if not self.can_attack:
      if current_time - self.attack_time >= self.attack_cooldown:
        self.can_attack = True
    if not self.vulnerable:
      if current_time - self.hit_time >= self.invincibility_duration:
        self.vulnerable = True

  def get_damage(self, player, attack_type):
    # Apply damage to the enemy based on player's attack type
    if self.vulnerable:
      self.hit_sound.play()
      self.direction = self.get_player_distance_direction(player)[1]
      if attack_type == 'weapon':
        self.health -= player.get_full_weapon_damage()
      else:
        self.health -= player.get_full_magic_damage()
      self.hit_time = pygame.time.get_ticks()
      self.vulnerable = False

  def check_death(self):
    # Check if the enemy has been defeated
    if self.health <= 0:
      self.kill()
      self.trigger_death_particles(self.rect.center, self.monster_name)
      self.add_exp(self.exp)
      self.death_sound.play()

  def hit_reaction(self):
    # Apply hit reaction if the enemy is not vulnerable
    if not self.vulnerable:
      self.direction *= -self.resistance

  def update(self):
    # Update the enemy's state and perform necessary actions
    self.hit_reaction()
    self.move(self.speed)
    self.animate()
    self.cooldown()
    self.check_death()

  def enemy_update(self, player):
    # Update the enemy based on the player's position
    self.get_status(player)
    self.actions(player)
