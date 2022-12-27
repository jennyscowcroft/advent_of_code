with open("input.txt") as f:
    instructions = f.read().splitlines()

x = 1
cycle = 1
cycles_list = [1]
x_list = [1]
intervals = [20, 60, 100, 140, 180, 220]
signal_strengths = []


for line in instructions:
    cycle += 1
    cycles_list.append(cycle)
    x_list.append(x)
    if line[0] == "a":
        x += int(line[5:])
        cycle += 1
        cycles_list.append(cycle)
        x_list.append(x)
    else:
        pass

for i in range(len(cycles_list)):
    if cycles_list[i] in intervals:
        signal_strength = cycles_list[i] * x_list[i]
        signal_strengths.append(signal_strength)

print(signal_strengths)
print(f"Total: {sum(signal_strengths)}")


CRT = [["."] * 40 for i in range(6)]
print(list(zip(cycles_list, x_list)))

for row in range(6):
    for column in range(40):
        place = row * 40 + column + 1
        if abs(x_list[place-1]-column) <= 1:
            CRT[row][column] = "#"

for i in CRT:
    print(i)