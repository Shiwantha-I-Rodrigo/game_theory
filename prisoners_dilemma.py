import random


# (Player1, Player2)
PAYOFFS = {
    ('C', 'C'): (3, 3),  # Reward
    ('C', 'D'): (0, 5),  # Sucker, Temptation
    ('D', 'C'): (5, 0),  # Temptation, Sucker
    ('D', 'D'): (1, 1),  # Punishment
}


# STRATEGIES
def always_defect(my_history, opponent_history):
    return 'D'

def always_cooperate(my_history, opponent_history):
    return 'C'

def tit_for_tat(my_history, opponent_history):
    if not opponent_history:
        return 'C'
    return opponent_history[-1]

def grim_trigger(my_history, opponent_history):
    if 'D' in opponent_history:
        return 'D'
    return 'C'

def pavlov(my_history, opponent_history):
    if not my_history:
        return 'C'
    
    last_my = my_history[-1]
    last_op = opponent_history[-1]
    payoff, _ = PAYOFFS[(last_my, last_op)]
    
    # Good payoff = 3 or 5
    if payoff >= 3:
        return last_my  # Stay
    else:
        return 'D' if last_my == 'C' else 'C'  # Shift

def generous_tft(my_history, opponent_history, forgiveness_prob=0.3):
    if not opponent_history:
        return 'C'
    
    if opponent_history[-1] == 'D':
        if random.random() < forgiveness_prob:
            return 'C'
        return 'D'
    return 'C'

def suspicious_tft(my_history, opponent_history):
    if not my_history:
        return 'D'
    return opponent_history[-1]

def random_strategy(my_history, opponent_history):
    return random.choice(['C', 'D'])

def adaptive_strategy(my_history, opponent_history):
    if len(opponent_history) < 5:
        return 'C'
    
    coop_rate = opponent_history.count('C') / len(opponent_history)
    
    # If opponent cooperates often --> cooperate
    if coop_rate > 0.6:
        return 'C'
    else:
        return 'D'


def play_round(strategy1, strategy2, history1, history2):
    move1 = strategy1(history1, history2)
    move2 = strategy2(history2, history1)
    
    payoff1, payoff2 = PAYOFFS[(move1, move2)]
    
    history1.append(move1)
    history2.append(move2)
    
    return payoff1, payoff2


def play_game(strategy1, strategy2, rounds=100):
    history1, history2 = [], []
    score1, score2 = 0, 0
    
    for _ in range(rounds):
        p1, p2 = play_round(strategy1, strategy2, history1, history2)
        score1 += p1
        score2 += p2
    
    return score1, score2


def tournament(strategies, rounds=200):
    results = {name: 0 for name in strategies}
    
    for name1, strat1 in strategies.items():
        for name2, strat2 in strategies.items():
            if name1 != name2:
                score1, _ = play_game(strat1, strat2, rounds)
                results[name1] += score1
    
    return results


strategies = {
    "ALLD": always_defect,
    "ALLC": always_cooperate,
    "TFT": tit_for_tat,
    "Grim Trigger": grim_trigger,
    "Pavlov": pavlov,
    "Generous TFT": generous_tft,
    "Suspicious TFT": suspicious_tft,
    "Random": random_strategy,
    "Adaptive": adaptive_strategy
}

results = tournament(strategies, rounds=300)

print("Tournament Results:\n")
for name, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {score}")
