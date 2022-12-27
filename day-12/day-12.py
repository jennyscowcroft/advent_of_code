with open("map.txt") as f:
    height_map = f.read().splitlines()

# unpack each list item to individual points
for i in range(len(height_map)):
    height_map[i] = [*height_map[i]]

# setup for Djikstra
S = set()
Q = []

PART = 2

# locate start and end
# if part 2, add all "a" points as possible starting points for Djikstra
for row in range(0,len(height_map)-1):
    for column in range(0,len(height_map[row])-1):
        if "S" in height_map[row][column]:
            height_map[row][column] = "a"
            Q.append(((row,column), 0))
        if "E" in height_map[row][column]:
            end_row = row
            end_column = column
        if "a" in height_map[row][column] and PART == 2:
            Q.append(((row, column), 0))

# surrounding square directions
directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

# Djikstra's algorithm
while Q:
    ((row, column), distance) = Q.pop(0)
    if (row, column) in S:
        continue
    S.add((row, column))
    if height_map[row][column] == "E":
        print(f"Highest point reached after {distance} steps")
        break
    for column_dir, row_dir in directions:
        new_row = row + row_dir
        new_column = column + column_dir
        if 0 <= new_column < len(height_map[0]) and  0 <= new_row < len(height_map):
            if height_map[new_row][new_column] == "E":
                value = ord("z")
            else:
                value = ord(height_map[new_row][new_column])
            if value - ord(height_map[row][column]) <= 1:
                Q.append(((new_row, new_column), distance + 1))




