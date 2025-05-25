# 🚀 Asteroids

Welcome to **Asteroids** – a modern Python remake of the classic arcade game!  
Dodge, shoot, and split asteroids as you pilot your nimble spaceship through the void. Can you survive the cosmic chaos and rack up a high score?
Created as part of the [Boot.dev curriculum](http://boot.dev/courses/build-asteroids-python).

---

## 🎮 How to Play

- **W / S**: Thrust forward / backward  
- **A / D**: Rotate your ship  
- **Spacebar**: Fire your blaster  
- **Avoid**: Colliding with asteroids (one hit and it’s game over!)

Shoot large asteroids to split them into smaller, faster ones. Destroy all asteroids to keep the galaxy safe (and your score climbing)!

---

## 🛠️ How It Works

- **Pygame** powers the graphics, input, and game loop.
- **Sprite Groups** manage all moving objects (player, asteroids, shots).
- **Collision Detection** uses simple circle math for fast, accurate results.
- **Asteroid Splitting**: Big rocks break into smaller ones when shot, just like the original.
- **Screen Wrapping**: Fly off one edge, reappear on the other—space is round!
- **Score System**: Earn points for every asteroid you blast.

---

## 🚀 Getting Started

1. **Install dependencies**  
   ```bash
   pip install pygame
   ```

2. **Run the game**  
   ```bash
   python3 main.py
   ```

3. **Have fun!**  
   Try to beat your high score and avoid cosmic doom!

---

## 📁 Project Structure

```
asteroids/
├── main.py           # Game loop and setup
├── constants.py      # All game constants
├── player.py         # Player spaceship logic
├── asteroid.py       # Asteroid logic and splitting
├── asteroidfield.py  # Spawns new asteroids
├── shot.py           # Bullet logic
├── circleshape.py    # Base class for circular objects
└── ...
```

---

## 🧑‍💻 Want to Hack On It?

- Try adding power-ups, new weapons, or visual effects!
- Make the asteroids lumpy, or add a shield!
- PRs and suggestions welcome!

---

**Enjoy blasting asteroids! 🚀**