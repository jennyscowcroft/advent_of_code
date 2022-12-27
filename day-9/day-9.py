with open("motions.txt") as f:
    motions = f.read().splitlines()

hx, hy = 0, 0
tx, ty = 0, 0
knots = [[0, 0] for i in range(0,10)]

visited_coords_p1 = set()
visited_coords_p1.add((tx, ty))

visited_coords_p2 = set()
visited_coords_p2.add((knots[9][0], knots[9][1]))

for motion in motions:
    direction = motion[0]
    steps = int(motion[2:])
    for step in range(steps):
        if direction == "R":
            hx += 1
            knots[0][0] += 1
        elif direction == "L":
            hx -= 1
            knots[0][0] -= 1
        elif direction == "U":
            hy += 1
            knots[0][1] += 1
        elif direction == "D":
            hy -= 1
            knots[0][1] -= 1

        if not (abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
            if not(hx == tx):
                tx += int((hx-tx)/abs(hx-tx))
            if not(hy == ty):
                ty += int((hy-ty)/abs(hy-ty))

        visited_coords_p1.add((tx, ty))

        for knot in range(1,10):
            ahead_x, ahead_y = knots[knot-1]
            current_x, current_y = knots[knot]
            if not (abs(ahead_x - current_x) <= 1 and abs(ahead_y - current_y) <= 1):
                if not (ahead_x == current_x):
                    current_x += int((ahead_x - current_x) / abs(ahead_x - current_x))
                if not (ahead_y == current_y):
                    current_y += int((ahead_y - current_y) / abs(ahead_y - current_y))
            knots[knot] = current_x, current_y

        visited_coords_p2.add((knots[9][0], knots[9][1]))
print(visited_coords_p1)
print(len(visited_coords_p1))
print(visited_coords_p2)
print(len(visited_coords_p2))
