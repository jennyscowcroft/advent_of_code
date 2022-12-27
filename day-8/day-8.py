with open("trees.txt") as f:
    tree_array = f.read().splitlines()

# Initialise visible trees with those on the edges (subtract 4 to account for duplicates on corners)
visible_trees = len(tree_array) * 2 + len(tree_array[0]) * 2 - 4
grid_y = len(tree_array)
grid_x = len(tree_array[0])

scores = []

for row in range(1, grid_y - 1):
    for column in range(1, grid_x - 1):
        current_tree = tree_array[row][column]

        # make list of trees to the left, right, above and below current tree
        left_trees = [tree_array[row][column - x] for x in range(1, column + 1)]
        right_trees = [tree_array[row][column + x] for x in range(1, grid_x - column)]
        up_trees = [tree_array[row - y][column] for y in range(1, row + 1)]
        down_trees = [tree_array[row + y][column] for y in range(1, grid_y - row)]

        # Part 1: find if the current tree is the biggest of surrounding trees
        if max(left_trees) < current_tree or max(right_trees) < current_tree or \
                max(up_trees) < current_tree or max(down_trees) < current_tree:
            visible_trees += 1

        # Part 2: calculate scenic score
        score = 1  # initialise viewing distance
        for trees in (left_trees, right_trees, up_trees, down_trees):
            distance = 0
            for i in range(len(trees)):
                if trees[i] < current_tree:
                    distance += 1
                elif trees[i] >= current_tree:
                    distance += 1
                    break
            score *= distance
            print(score)
        scores.append(score)
print(visible_trees)
print(scores)
print(max(scores))
