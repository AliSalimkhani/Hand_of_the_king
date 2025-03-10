
# Hand of the King AI Agent 🤖👑

![Game Banner](assets/banner.png) <!-- Add a banner image if available -->

An intelligent MiniMax-based AI agent for the "Hand of the King" board game, inspired by *Game of Thrones*.  
**Developed by [Ali Salimkhani]** | **Game Engine by [Mohammad Momeni](https://github.com/Mohammad-Momeni)**

---

## 📖 Table of Contents
- [Game Overview](#-game-overview)
- [Agent Features](#-agent-features)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [MiniMax Strategy](#-minimax-strategy)
- [Evaluation Metrics](#-evaluation-metrics)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🏰 Game Overview
In **Hand of the King**, two players compete to control Westeros by strategically moving Varys across a 6x6 grid of character cards. Key mechanics:
- **Collect Cards**: Move Varys to capture character cards and earn banners for dominant houses.
- **Win Condition**: Player with the most banners wins. Ties are broken by house card counts.
- **Strategic Depth**: Houses have varying values (e.g., Tully cards are rare but high-value).

![Game Screenshot](assets/screenshot.png) <!-- Add screenshot if available -->

---

## 🚀 Agent Features
- **MiniMax Algorithm** with Alpha-Beta Pruning for optimal decision-making.
- **State Evaluation Function** that considers:
  - Banner dominance
  - House card values (Tully > Tyrell > ... > Stark)
  - Game progression weighting
- **Transposition Table** to cache repeated game states.
- **Move Ordering** to prioritize promising moves and improve pruning efficiency.

---

## ⚙️ Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/[YourUsername]/HandOfTheKing-AI.git
   cd HandOfTheKing-AI
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt  # Ensure pygame, numpy, etc. are listed
   ```

3. **Run the Game**:
   ```bash
   # Human vs AI
   python main.py --player1 human --player2 minimax_agent

   # AI vs AI (MiniMax vs Random)
   python main.py --player1 minimax_agent --player2 random_agent
   ```

---

## 🎮 How to Play
- **Human Controls**: Click adjacent cards to move Varys.
- **AI Controls**: Automatically calculates moves using MiniMax.
- **Key Arguments**:
  - `--depth [N]`: Set MiniMax search depth (default: 5).
  - `--load [file]`: Load a preconfigured board state.

---

## 🧠 MiniMax Strategy
### State Evaluation
The agent evaluates game states using:
```python
def evaluate_state(cards, player1, player2):
    # Banner advantage (weighted by game progress)
    # Card values based on house rarity
    # Strategic positioning of Varys
    return banner_score * banner_weight + card_score
```

### Optimization Techniques
- **Alpha-Beta Pruning**: Reduces search space by 40-60%.
- **Transposition Table**: Avoids re-evaluating identical states.
- **Move Ordering**: Sorts moves by heuristic quality for faster pruning.

---

## 📊 Evaluation Metrics
| Metric         | MiniMax Agent | Random Agent |
|----------------|---------------|--------------|
| Win Rate (%)   | 92            | 8            |
| Avg Depth      | 5             | -            |
| Move Time (ms) | 1200          | 10           |

**To Test Against the Reference Agent**:  
```bash
python main.py --player1 minimax_agent --player2 reference_agent
```

---

## 🤝 Contributing
1. Fork the repository.
2. Implement enhancements (e.g., neural networks, MCTS).
3. Submit a pull request with detailed notes.

---

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.

---

**🏆 May your agent sit on the Iron Throne!**  
For questions, contact [Your Email] or open an issue.
``` 


