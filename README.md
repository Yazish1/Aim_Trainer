# 🎯 Aim trainer (Pygame)

A simple aim training game built using python and Pygame.
The goal is to test and improve mouse accuracy by clicking targets before losing all HP

---

# Gameplay Overview

- Start at the **Level Select** screen
- Choose a level
- Click targets to increase your score
- Missing targets reduces HP
- Each level ends when:
  - Score threshold is reached (win) (Originally set to 30)
  - HP reaches zero (loss)

After a game ends, you can:

- Return to level section
- Press ESC to exit the game

## Controls

| Action                   | Input             |
| ------------------------ | ----------------- |
| Click target             | Left mouse button |
| Exit (menus / game over) | ESC               |
| Exit game                | Close window (X)  |

## Tools

- Python
- Pygame

## To play the game

1. Clone the repository

```
git clone https://github.com/Yazish1/Aim_Trainer
```

2. Install dependencies

```
pip install pygame
```

3. Run the game

```
python game.py
```
