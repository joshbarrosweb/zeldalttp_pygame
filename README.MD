# Zelda Link To The Past CLONE

This project is a recreation of the classic The Legend of Zelda: A Link to the Past game implemented in Python using the Pygame library.

## Special Thanks

Special thanks to the original Zelda game developers for inspiring this project!

## Project Structure

The project has the following file and folder structure:

### `src`

This folder contains the source code files for the game:

- `main.py`: The main entry point of the game. It sets up the game, initiates the game loop, and manages the main game objects and logic.
- `debug.py`: Contains debugging functionalities for the game.
- `enemy.py`: Contains the `Enemy` class which represents the enemy entities in the game and defines their behavior and interactions with the player.
- `entity.py`: Contains the `Entity` class, a base class for all game characters, handling shared characteristics like movement, animation, health, and damage.
- `level.py`: Handles level structure and progression.
- `magic.py`: Manages magic abilities and their effects.
- `particles.py`: Handles the particle effects in the game.
- `player.py`: Contains the `Player` class which represents the player character, handling player movement, interactions, health tracking, and input handling.
- `settings.py`: Contains global game settings and constants, such as window size and paths to assets.
- `support.py`: Contains utility functions and classes for support operations such as file imports.
- `tile.py`: Contains the `Tile` class which represents the tiles in the game world and their properties.
- `ui.py`: Manages the user interface elements such as health bar, magic meter and other in-game displays.
- `upgrade.py`: Manages the upgrading mechanics of the game, including but not limited to, upgrading player stats and weapons.
- `weapon.py`: Handles the different types of weapons in the game.

### `resources`

This folder contains various resources used in the game:

- `graphics`: Contains the game's graphic files, organized into folders for different types of graphics, such as player, enemy, and backgrounds.
- `audio`: Contains the game's sound files, including sound effects and background music.

## Instructions

To run the project, follow these steps:

1. Install Python 3 if you haven't already.
2. Install the Pygame library by running the command: `pip install pygame`.
3. Clone or download the project files to your local machine.
4. Navigate to the project directory.
5. Run the command: `python3 src/main.py`.

Make sure you have the required resources in the appropriate directories as shown in the folder structure.

Feel free to modify and explore the game to suit your needs.

Enjoy playing!
