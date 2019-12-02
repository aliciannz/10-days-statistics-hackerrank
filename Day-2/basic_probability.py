dice = [1,2,3,4,5,6]

total_outcomes = len(dice) * len(dice)
favorable_outcomes = 0
for i in range(len(dice)):
    for j in range(len(dice)):
        if dice[i] + dice[j] <= 9:
            favorable_outcomes = favorable_outcomes + 1


print(total_outcomes)
print(favorable_outcomes)
print(favorable_outcomes / total_outcomes)