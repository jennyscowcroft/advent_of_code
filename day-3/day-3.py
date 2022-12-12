def convert_score(char):
    if "a" <= char <= "z":
        return ord(char) - 96
    else:
        return ord(char) - 38


with open("rucksacks.txt") as f:
    ruck_list = f.read().splitlines()

# Part 1
p1_total = 0
for i in ruck_list:
    first_half = i[:len(i) // 2]
    second_half = i[len(i) // 2:]
    for n in first_half:
        if n in second_half:
            p1_total += convert_score(n)
            break
print(p1_total)

# Part 2
p2_total = 0
j = 0
while j < len(ruck_list):
    for char in ruck_list[j]:
        if char in ruck_list[j + 1] and char in ruck_list[j + 2]:
            print(char)
            [print(convert_score(char))]
            p2_total += convert_score(char)
            break
    j += 3

print(p2_total)
