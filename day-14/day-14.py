with open("structures.txt") as f:
    lines = f.read().splitlines()

rocks = set()

for line in lines:
    prev_rock = None
    for coord in line.split(" -> "):
        x, y = map(int, coord.split(","))
        if prev_rock is not None:
            dx = x - prev_rock[0]
            dy = y - prev_rock[1]
            length = max(abs(dx), abs(dy))
            for i in range(length + 1):
                x_struct = prev_rock[0] + i * (1 if dx > 0 else -1 if dx < 0 else 0)
                y_struct = prev_rock[1] + i * (1 if dy > 0 else -1 if dy < 0 else 0)
                rocks.add((x_struct, y_struct))

        prev_rock = (x, y)


# Part One
def part_one():
    abyss = False
    sand = set()
    max_y = max(coord[1] for coord in rocks)

    while not abyss:
        new_sand = (500, 0)
        curr_sand = new_sand
        stopped = False
        while not stopped:
            if curr_sand[1] > max_y:
                abyss = True
                break
            for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
                next_sand = (curr_sand[0] + dx, curr_sand[1] + dy)
                if next_sand not in rocks and next_sand not in sand:
                    curr_sand = next_sand
                    break
            else:
                stopped = True
                sand.add(curr_sand)
    return (len(sand))


def part_two():
    sand = set()
    max_y = max(coord[1] for coord in rocks) + 1
    while ((500, 0) not in sand):
        new_sand = (500, 0)
        curr_sand = new_sand
        stopped = False
        while not stopped:
            if curr_sand[1] >= max_y:
                stopped = True
                sand.add(curr_sand)
            for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
                next_sand = (curr_sand[0] + dx, curr_sand[1] + dy)
                if next_sand not in rocks and next_sand not in sand:
                    curr_sand = next_sand
                    break
            else:
                stopped = True
                sand.add(curr_sand)
    return len(sand)

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")
