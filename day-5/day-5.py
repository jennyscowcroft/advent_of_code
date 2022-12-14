with open("procedure.txt") as f:
    stack_strings, instructions = [i.split("\n") for i in f.read().split("\n\n")]

# Create dictionary of stack lists
stack_p1 = {int(digit): [] for digit in stack_strings[-1].replace(" ", "")}
stack_p2 = {int(digit): [] for digit in stack_strings[-1].replace(" ", "")}

# Create list of crates with only crate ID letters and exclude indexes
crates = [list(char[1::4]) for char in stack_strings][:-1]

# Populate dictionary of stack lists
for row in crates:
    for i in range(len(row)):
        if row[i].isalnum():
            stack_p1[i + 1] += row[i]
            stack_p2[i + 1] += row[i]

# Reverse stacks
for row in stack_p1:
    stack_p1[row] = stack_p1[row][::-1]
    stack_p2[row] = stack_p2[row][::-1]

# Parse and execute instructions
for row in instructions:
    # Extract movement instructions
    amount, start, end = row.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
    amount, start, end = int(amount), int(start), int(end)
    print(amount, start, end)

    # Rearrange as described in part 1
    moved_crates = stack_p1[start][-amount:]
    moved_crates.reverse()
    stack_p1[end] += moved_crates
    stack_p1[start] = stack_p1[start][:-amount]

    # Rearrange as described in part 2
    stack_p2[end] += stack_p2[start][-amount:]
    stack_p2[start] = stack_p2[start][:-amount]

# Print top of each stack
print("Part 1: ")
for row in stack_p1:
    print(stack_p1[row][-1])

print("Part 2: ")
for row in stack_p2:
    print(stack_p2[row][-1])



