with open("strategy.txt") as strategy_file:
    strategy_text = strategy_file.read().splitlines()
#Part 1
p1_score = 0
p1_scores = {"A X": 4, "A Y": 8, "A Z": 3,
          "B X": 1, "B Y": 5, "B Z": 9,
          "C X": 7, "C Y": 2, "C Z": 6}

for i in strategy_text:
    if i in p1_scores:
        p1_score += p1_scores[i]
print(p1_score)

#Part 2
p2_score = 0
p2_scores = {"A X": 3, "A Y": 4, "A Z": 8,
          "B X": 1, "B Y": 5, "B Z": 9,
          "C X": 2, "C Y": 6, "C Z": 7}

for i in strategy_text:
    if i in p2_scores:
        p2_score += p2_scores[i]
print(p2_score)