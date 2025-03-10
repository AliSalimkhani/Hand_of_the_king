import mathimport copyfrom random_agent import get_valid_movesfrom main import make_move, find_varysfrom utils.classes import Card, Playerdef evaluate_state(cards, player1, player2):    """    Enhanced evaluation function for Hand of the King.    Focuses on banners, card values, and strategic control of Varys's movement.    """    # Banner advantage    banner_score = sum(player1.get_banners().values()) - sum(player2.get_banners().values())    # Evaluate card values    card_values = {  # Example card values - adjust as needed        "Varys": 0,     # Neutral value for Varys        # Add values for other cards if applicable    }    player1_card_score = sum(        card_values.get(card.get_name(), 1) for house, card_list in player1.get_cards().items() for card in card_list    )    player2_card_score = sum(        card_values.get(card.get_name(), 1) for house, card_list in player2.get_cards().items() for card in card_list    )    card_score = player1_card_score - player2_card_score    # Remaining cards in play    remaining_cards = len(cards)    banner_weight = 1 + (36 - remaining_cards) * 0.1  # Increase banner weight as the game progresses    return banner_score * banner_weight + card_scoredef evaluate_move(move, cards, player1, player2):    """    Evaluate a single move by simulating it and calculating the resulting state score.    """    new_cards = copy.deepcopy(cards)    new_player1 = copy.deepcopy(player1)    new_player2 = copy.deepcopy(player2)    make_move(new_cards, move, new_player1)    return evaluate_state(new_cards, new_player1, new_player2)def minimax(cards, player1, player2, depth, alpha, beta, maximizing_player, transposition_table):    """    Minimax algorithm with alpha-beta pruning and transposition table.    """    # Hashable representation of the game state    state_hash = tuple((card.get_house(), card.get_name(), card.get_location()) for card in cards)    if (state_hash, maximizing_player) in transposition_table:        return transposition_table[(state_hash, maximizing_player)]    if depth == 0 or not get_valid_moves(cards):        eval_val = evaluate_state(cards, player1, player2)        transposition_table[(state_hash, maximizing_player)] = eval_val, None        return eval_val, None    if maximizing_player:        max_eval = -math.inf        best_move = None        moves = get_valid_moves(cards)        moves.sort(key=lambda move: evaluate_move(move, cards, player1, player2), reverse=True)  # Move ordering        for move in moves:            new_cards = copy.deepcopy(cards)            new_player1 = copy.deepcopy(player1)            new_player2 = copy.deepcopy(player2)            make_move(new_cards, move, new_player1)            eval, _ = minimax(new_cards, new_player1, new_player2, depth - 1, alpha, beta, False, transposition_table)            if eval > max_eval:                max_eval = eval                best_move = move            alpha = max(alpha, eval)            if beta <= alpha:                break        transposition_table[(state_hash, maximizing_player)] = max_eval, best_move        return max_eval, best_move    else:        # Minimizing player        min_eval = math.inf        best_move = None        moves = get_valid_moves(cards)        moves.sort(key=lambda move: evaluate_move(move, cards, player1, player2))  # Move ordering for minimizing player        for move in moves:            new_cards = copy.deepcopy(cards)            new_player1 = copy.deepcopy(player1)            new_player2 = copy.deepcopy(player2)            make_move(new_cards, move, new_player2)            eval, _ = minimax(new_cards, new_player1, new_player2, depth - 1, alpha, beta, True, transposition_table)            if eval < min_eval:                min_eval = eval                best_move = move            beta = min(beta, eval)            if beta <= alpha:                break        transposition_table[(state_hash, maximizing_player)] = min_eval, best_move        return min_eval, best_movedef get_move(cards, player1, player2):    """    Determine the best move for the maximizing player using minimax.    """    transposition_table = {}  # Initialize the transposition table    _, move = minimax(cards, player1, player2, depth=5, alpha=-math.inf, beta=math.inf, maximizing_player=True, transposition_table=transposition_table)    return move