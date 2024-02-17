import copy

# Represent a card deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# Define Shithead game rules
def is_valid_move(card, pile):
    if not pile:
        return True
    last_card_rank = pile[-1]['rank']
    return ranks.index(card['rank']) > ranks.index(last_card_rank)

def is_special_card(card):
    return card['rank'] in ['8', '10']

def is_finished(player_hand):
    return not player_hand

# Evaluate the score for a given hand
def evaluate_hand(hand):
    return sum(ranks.index(card['rank']) + 1 for card in hand)

# Perform a depth-first search to find the optimal moves
def dfs(player_hand, pile, depth, maximizing_player):
    if depth == 0 or is_finished(player_hand):
        return evaluate_hand(player_hand)

    if maximizing_player:
        max_eval = float('-inf')
        for card in player_hand:
            if is_valid_move(card, pile):
                new_player_hand = [c for c in player_hand if c != card]
                new_pile = pile + [card]
                eval_score = dfs(new_player_hand, new_pile, depth - 1, False)
                max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for card in player_hand:
            if is_valid_move(card, pile):
                new_player_hand = [c for c in player_hand if c != card]
                new_pile = pile + [card]
                eval_score = dfs(new_player_hand, new_pile, depth - 1, True)
                min_eval = min(min_eval, eval_score)
        return min_eval

# Find the optimal move using the depth-first search algorithm
def find_optimal_move(player_hand, pile, depth):
    optimal_score = float('-inf')
    optimal_move = None

    for card in player_hand:
        if is_valid_move(card, pile):
            new_player_hand = [c for c in player_hand if c != card]
            new_pile = pile + [card]
            eval_score = dfs(new_player_hand, new_pile, depth - 1, False)

            if eval_score > optimal_score:
                optimal_score = eval_score
                optimal_move = card

    return optimal_move

# Example usage
player_hand = deck[:10]  # Initial hand for the player
pile = []  # Pile of played cards
depth = 3  # Depth of the search algorithm

optimal_move = find_optimal_move(player_hand, pile, depth)
print("Optimal Move:", optimal_move)

