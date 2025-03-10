import math
import copy
from random_agent import get_valid_moves
from main import make_move


def evaluate_state(cards, player1, player2):
    """
    Enhanced evaluation function for Hand of the King.
    Focuses on banners, card values, and strategic control of Varys's movement.
    """
    # Calculate the difference in banner scores between the two players
    banner_score = sum(player1.get_banners().values()) - sum(player2.get_banners().values())

    # Define card values for different houses based on their rarity
    card_values = {
        "Stark": 0.1,  # 8 cards, least valuable
        "Greyjoy": 0.15,  # 7 cards
        "Lannister": 0.2,  # 6 cards
        "Targaryen": 0.25,  # 5 cards
        "Baratheon": 0.3,  # 4 cards
        "Tyrell": 0.35,  # 3 cards
        "Tully": 0.4,  # 2 cards, most valuable
    }

    # Calculate card scores for both players by summing up the values of their cards
    player1_card_score = sum(
        card_values.get(card.get_house(), 1) for house, card_list in player1.get_cards().items() for card in card_list
    )
    player2_card_score = sum(
        card_values.get(card.get_house(), 1) for house, card_list in player2.get_cards().items() for card in card_list
    )
    card_score = player1_card_score - player2_card_score

    print(f"Evaluate State -> Banner Score: {banner_score}, Card Score: {card_score}")

    return banner_score * card_score


# Function to simulate a move and evaluate the resulting state
def evaluate_move(move, cards, player1, player2):
    """
    Evaluate a single move by simulating it and calculating the resulting state score.
    """
    # Deep copy the current game state to simulate the move
    new_cards = copy.deepcopy(cards)
    new_player1 = copy.deepcopy(player1)
    new_player2 = copy.deepcopy(player2)

    # Apply the move and evaluate the new state
    make_move(new_cards, move, new_player1)
    state_score = evaluate_state(new_cards, new_player1, new_player2)
    print(f"Evaluate Move -> Move: {move}, State Score: {state_score}")
    return state_score


# Minimax function with alpha-beta pruning (without transposition table)
def minimax(cards, player1, player2, depth, alpha, beta, maximizing_player):
    """
    Minimax algorithm with alpha-beta pruning.
    """
    # Base case: evaluate the state if depth is 0 or no valid moves are left
    if depth == 0 or not get_valid_moves(cards):
        eval_val = evaluate_state(cards, player1, player2)
        print(f"Minimax Base Case -> Depth: {depth}, Eval: {eval_val}")
        return eval_val, None

    if maximizing_player:
        # Maximizing player logic
        max_eval = -math.inf
        best_move = None
        moves = get_valid_moves(cards)
        # Sort moves to optimize alpha-beta pruning
        moves.sort(key=lambda move: evaluate_move(move, cards, player1, player2), reverse=True)

        for move in moves:
            # Simulate the move for the maximizing player
            new_cards = copy.deepcopy(cards)
            new_player1 = copy.deepcopy(player1)
            new_player2 = copy.deepcopy(player2)
            make_move(new_cards, move, new_player1)
            eval, _ = minimax(new_cards, new_player1, new_player2, depth - 1, alpha, beta, False)
            print(f"Maximizing -> Move: {move}, Eval: {eval}, Alpha: {alpha}, Beta: {beta}")
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                print("Pruning in Maximizing Player")
                break  # Prune the search tree
        print(f"Maximizing Player -> Depth: {depth}, Best Move: {best_move}, Eval: {max_eval}")
        return max_eval, best_move
    else:
        # Minimizing player logic
        min_eval = math.inf
        best_move = None
        moves = get_valid_moves(cards)
        # Sort moves to optimize alpha-beta pruning
        moves.sort(key=lambda move: evaluate_move(move, cards, player1, player2))

        for move in moves:
            # Simulate the move for the minimizing player
            new_cards = copy.deepcopy(cards)
            new_player1 = copy.deepcopy(player1)
            new_player2 = copy.deepcopy(player2)
            make_move(new_cards, move, new_player2)
            eval, _ = minimax(new_cards, new_player1, new_player2, depth - 1, alpha, beta, True)
            print(f"Minimizing -> Move: {move}, Eval: {eval}, Alpha: {alpha}, Beta: {beta}")
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Prune the search tree
        print(f"Minimizing Player -> Depth: {depth}, Best Move: {best_move}, Eval: {min_eval}")
        return min_eval, best_move


# Function to determine the best move for the maximizing player
def get_move(cards, player1, player2):
    """
    Determine the best move for the maximizing player using minimax.
    """
    _, move = minimax(cards, player1, player2, depth=2, alpha=-math.inf, beta=math.inf, maximizing_player=True)
    print(f"Best Move Found -> {move}")
    return move