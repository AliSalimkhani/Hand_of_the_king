# Hand of the King AI Agent

An intelligent MiniMax-based AI agent for the "Hand of the King" board game, inspired by *Game of Thrones*.

Developed by Ali Salimkhani  
Game Engine by [Mohammad Momeni](https://github.com/Mohammad-Momeni/Hand-of-the-King)

---

## Table of Contents

- [Game Overview](#game-overview)
- [Agent Features](#agent-features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [MiniMax Strategy](#minimax-strategy)
- [Evaluation Metrics](#evaluation-metrics)
- [Contributing](#contributing)
- [License](#license)

---

## Game Overview

Hand of the King is a two-player competitive strategy game played on a 6x6 grid of character cards. Players move Varys to collect house cards and acquire banners. The player with the most banners wins. In case of a tie, the winner is determined by the total number of cards of tied houses.

Strategic complexity arises from the differing rarity and value of house cards. For example, Tully cards offer a higher value-to-rarity ratio compared to houses like Stark.

<!-- Add game screenshot if available -->

---

## Agent Features

- MiniMax search with Alpha-Beta Pruning.
- State evaluation function considering:
  - Banner control advantage.
  - House-specific card values (e.g., Tully > Tyrell > Baratheon > Stark).
  - Temporal weighting based on game progression.
- Transposition table to avoid re-evaluating previously seen states.
- Move ordering for more efficient pruning.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AliSalimkhani/HandOfTheKing-AI.git
cd HandOfTheKing-AI
````

---

## How to Play

### Human vs AI

```bash
python main.py --player1 human --player2 minimax_agent
```

### AI vs AI (MiniMax vs Random)

```bash
python main.py --player1 minimax_agent --player2 random_agent
```

### Controls

* Human: Click on adjacent cards to move Varys.
* AI: Automatically selects optimal move using MiniMax.

### Optional Parameters

```bash
--depth [N]         # Set the MiniMax search depth (default: 5)
--load [file_path]  # Load a predefined board state from a file
```

---

## MiniMax Strategy

### Evaluation Function

```python
def evaluate_state(cards, player1, player2):
    # Calculates weighted sum of banner advantage and house card values
    return banner_score * banner_weight + card_score
```

### Optimizations

* **Alpha-Beta Pruning**: Prunes irrelevant branches of the search tree.
* **Transposition Table**: Caches evaluated states to avoid redundancy.
* **Move Ordering**: Sorts moves to maximize pruning effectiveness.

---

## Evaluation Metrics

| Metric         | MiniMax Agent | Random Agent |
| -------------- | ------------- | ------------ |
| Win Rate (%)   | 92            | 8            |
| Average Depth  | 5             | -            |
| Move Time (ms) | 1200          | 10           |

Run benchmark against a reference agent:

```bash
python main.py --player1 minimax_agent --player2 reference_agent
```

---

## Contributing

1. Fork the repository.
2. Implement new features or improvements (e.g., Neural Networks, MCTS).
3. Submit a pull request with detailed documentation of changes.

---

## License

MIT License. See [LICENSE](./LICENSE) for details.

---

## Contact

For technical questions or bug reports, contact:
[my email](mailto:alisalimkhani2004@gmail.com)
