from functools import cmp_to_key

with open("signals.txt") as f:
    pairs = f.read().strip().split("\n\n")

indices = []
packets = []


# Function to compare left and right sides
def compare_sides(left, right):
    # Both integers
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1

    # Both lists
    elif isinstance(left, list) and isinstance(right, list):
        n = 0
        while n < len(left) and n < len(right):
            compare_int = compare_sides(left[n], right[n])
            if compare_int == 1:
                return 1
            if compare_int == -1:
                return -1
            n += 1
        # Check if left is shorter than right
        if n == len(left) and n < len(right):
            return -1
        elif n == len(right) and n < len(left):
            return 1
        else:
            return 0

    # If one side is list and other is integer
    elif isinstance(left, list) and isinstance(right, int):
        return compare_sides(left, [right])

    elif isinstance(left, int) and isinstance(right, list):
        return compare_sides([left], right)


for index, pair in enumerate(pairs):
    pair_one, pair_two = pair.split("\n")
    pair_one = eval(pair_one)
    pair_two = eval(pair_two)
    packets.append(pair_one)
    packets.append(pair_two)
    if compare_sides(pair_one, pair_two) == -1:
        indices.append(index + 1)

print(f"Part 1: {sum(indices)}")

# Part 2
# append divider packets
packets.append([[2]])
packets.append([[6]])
index_product = 1

sorted_packets = sorted(packets, key=cmp_to_key(compare_sides))

# Find index of divider packets
for index, packet in enumerate(sorted_packets):
    if packet == [[2]] or packet == [[6]]:
        index_product *= index + 1

print(f"Part 2: {index_product}")
