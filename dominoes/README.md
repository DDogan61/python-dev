# Dominoes

A terminal-based Dominoes game where you play against the computer.

This project was completed as part of the [Hyperskill](https://hyperskill.org) **Python Developer** track.

- **Author:** Doğan Doğan
- **Completed:** 27.10.2026

## How to run

Requires Python 3.

```bash
python dominoes.py
```

## How to play

- The 28-piece domino set is shuffled; you and the computer each get 7 pieces, the rest form the stock.
- The player holding the highest double starts.
- On your turn, enter a number:
  - a **negative** number to place that piece on the **left** end of the snake,
  - a **positive** number to place it on the **right** end,
  - **0** to draw a piece from the stock (skip your turn).
- The game ends when a player runs out of pieces, or in a draw when no more moves are possible.

## What I practiced

- Building a program incrementally, stage by stage, without rewriting it from scratch
- Managing game state with lists and functions
- Input validation and turn-based game loop
- A simple AI that picks moves by scoring pieces based on number frequency