import numpy as np
import time

start = time.time()

with open('aoc/day8.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

trees = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
    trees[i, :] = np.array(list(line))

visible_trees = 2*len(lines[0]) + 2 *(len(lines)-2)

for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        meow = True
        tree_column = trees[:, j] - trees[i, j]
        tree_row = trees[i, :] - trees[i, j]
        '''
        routes = [list(tree_row[:j]), list(tree_row[j+1:]), list(tree_column[:i]), list(tree_column[i+1:])]
        print(routes)
        for j in range(len(routes)):
            #for k in range(len(routes[j])):
                if routes[j][k] > 0:
                    meow = False
        if meow:
            visible_trees +=1
        '''
        routes = [tree_row[:j], tree_row[j+1:], tree_column[:i], tree_column[i+1:]]
        if sum(list(map(lambda route: (route<0).all(), routes))) > 0:
            visible_trees += 1

print(visible_trees)
stop = time.time()

scenic_scores = np.zeros((len(lines), len(lines[0])), dtype=int)

def compute_scenic_score(route):
    big_trees_array = list(route >= 0)
    if True in big_trees_array:
        return big_trees_array.index(True) + 1
    else:
        return len(big_trees_array)

# iterate over trees
for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        tree_column = trees[:, j] - trees[i, j]
        tree_row = trees[i, :] - trees[i, j]
        # left, right, up, down
        routes = [tree_row[j-1::-1], tree_row[j+1:], tree_column[i-1::-1], tree_column[i+1:]]
        scenic_scores[i,j] = np.prod(list(map(compute_scenic_score, routes)))
    
print(np.max(scenic_scores))

print(stop - start)