from itertools import combinations

def calculate_score(card1, card2):
    if card1 == card2:
        return 20 + card1
    else:
        return (card1 + card2) % 10

def calculate_win_probability(a, b):
    my_score = calculate_score(a, b)
    
    cards = [i for i in range(1, 11) for _ in range(2)]
    cards.remove(a)
    cards.remove(b)
    
    opponent_combinations = list(combinations(cards, 2))
    
    win_count = 0
    for opp_card1, opp_card2 in opponent_combinations:
        opp_score = calculate_score(opp_card1, opp_card2)
        if my_score > opp_score:
            win_count += 1
            
    total_cases = len(opponent_combinations)
    
    win_probability = win_count / total_cases
    
    return win_probability

a, b = map(int, input().split())

win_probability = calculate_win_probability(a, b)

print(f"{win_probability:.3f}")
