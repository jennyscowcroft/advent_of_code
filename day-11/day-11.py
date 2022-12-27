with open("notes.txt") as f:
    lines = f.read().strip().split("\n\n")

items_held = []
op = []
condition = []
true_action = []
false_action = []
interactions = []
ROUNDS = 10000

for monkey in lines:
    monkey_number, starting, operation, test, true, false = monkey.split("\n")
    items_held.append([int(i) for i in starting.split(": ")[1].split(",")])
    op.append([i for i in operation.split("= ")[1].split(" ")])
    condition.append(int(test.split(" ")[-1]))
    true_action.append(int(true.split(" ")[-1]))
    false_action.append(int(false.split(" ")[-1]))
    interactions.append(0)

modulo_all = 1
for div in condition:
    modulo_all *= div

print(items_held)
for n in range(ROUNDS):
    print(n)
    for i in range(len(items_held)):
        for j in range(len(items_held[i])):
            interactions[i] += 1
            if op[i][1] == "+":
                if op[i][2] == "old":
                    items_held[i][j] += items_held[i][j]
                else:
                    items_held[i][j] += int(op[i][2])
            elif op[i][1] == "*":
                if op[i][2] == "old":
                    items_held[i][j] *= items_held[i][j]
                else:
                    items_held[i][j] *= int(op[i][2])
            if ROUNDS == 20:
                items_held[i][j] = items_held[i][j] // 3
            else:
                items_held[i][j] = items_held[i][j] % modulo_all

            if items_held[i][j] % condition[i] == 0:
                items_held[true_action[i]].append(items_held[i][j])
            else:
                items_held[false_action[i]].append(items_held[i][j])
        items_held[i] = []

sorted_interactions = sorted(interactions)
monkey_business = sorted_interactions[-1] * sorted_interactions[-2]
print(monkey_business)
