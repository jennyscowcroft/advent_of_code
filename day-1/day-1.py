with open("elves.txt") as elves_file:
    elves = elves_file.read()

elves_list = elves.split("\n\n")

separated_list = []
for n in elves_list:
    new_n = n.split("\n")
    separated_list.append(new_n)

totals = []
for i in separated_list:
    total = sum(int(x) for x in i)
    totals.append(total)

totals.sort()
max_calories = max(totals)
top_three_total = sum(totals[-3:])
print(max_calories)
print(top_three_total)
