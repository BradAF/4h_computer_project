# Star Trek: Asteroid Belt Evasion

This is a pygame-based game titled 'Star Trek: Asteroid Belt Evasion'. The objective of the game is to control a spaceship and navigate it through an endless field of asteroids. The spaceship can be moved left or right in order to avoid incoming asteroids.

The spaceship has to dodge the asteroids to keep the game going. If it collides with an asteroid, the game ends, and you can restart the game by pressing the space bar. Points are added to your score every second the spaceship stays in play.

## Prerequisites
To set up this game, you must have **Python** and **poetry** installed on your machine. You also need to install the required dependency using `poetry install` command, which uses the provided `pyproject.toml` file to install dependencies.

## Installation
Clone the repository on your local machine. You would find a `pyproject.toml` file which contains all the dependencies required for this game. Run the following command to install these dependencies:

```
poetry install
```

## Folder Structure
The game comes with a folder named `graphics/` which contains the graphic files, such as the ship and asteroid images, used in the game and a `font/` folder that contains the font used in the game. 

- `graphics/` : This folder contains various image assets for the game such as the spaceship, background, and asteroid images.
- `font/` : This folder contains the custom pixel font used in the game for the score and text messages.

## Starting the Game
Navigate to the folder containing the game file in your terminal, and run the following command to start the game:

```
poetry run python game.py
```

## Controls
You can control the spaceship using the following keyboard keys:

- `Arrow Right` or `d` : Move the spaceship to the right
- `Arrow Left` or `a` : Move the spaceship to the left
- `Space Bar` : Restart the game after the spaceship crashes into an asteroid
