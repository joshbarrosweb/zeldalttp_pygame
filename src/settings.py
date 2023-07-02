# Dimensions for game window
WIDTH = 1280
HEIGHT = 720

# Frame per second for game loop
FPS = 60

# Size of the tiles in the game
TILESIZE = 64

# Offsets for different hitboxes
HITBOX_OFFSET = {
  'player': -26,
  'object': -40,
  'grass': -10,
  'invisible': 0
}

# Dimensions for the UI bars
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80

# Font settings for UI
UI_FONT = './resources/font/joystix.ttf'
UI_FONT_SIZE = 18

# Color settings for UI and water
WATER_COLOR = '#71DDEE'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# Data for the various weapons in the game
weapon_data = {
  'sword': {'cooldown': 100, 'damage': 15, 'graphic': './resources/weapons/sword/full.png'},
  'lance': {'cooldown': 400, 'damage': 30, 'graphic': './resources/weapons/lance/full.png'},
  'axe': {'cooldown': 300, 'damage': 20, 'graphic': './resources/weapons/axe/full.png'},
  'rapier': {'cooldown': 50, 'damage': 8, 'graphic': './resources/weapons/rapier/full.png'},
  'sai': {'cooldown': 80, 'damage': 10, 'graphic': './resources/weapons/sai/full.png'}
}

# Data for the different magic abilities in the game
magic_data = {
  'flame': {'strength': 5, 'cost': 20, 'graphic': './resources/particles/flame/fire.png'},
  'heal': {'strength': 5, 'cost': 10, 'graphic': './resources/particles/heal/heal.png'}
}

# Data for the various monsters in the game
monster_data = {
  'squid': { 'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': './resources/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
  'raccoon': { 'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': './resources/audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
  'spirit': { 'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': './resources/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
  'bamboo': { 'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': './resources/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 360},
}
