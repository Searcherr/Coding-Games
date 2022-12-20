import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input('Enter the number of nodes: '))  # This variables stores how many nodes are given
nodes_array = np.zeros(shape=(n, 2))
for i in range(n):
    # x: The x coordinate of the given node
    # y: The y coordinate of the given node
    x, y = [int(j) for j in input().split()]
    nodes_array[i] = [x, y]


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# You have to output a valid path
print('x = ', x)
print('y = ', y)
print(nodes_array)
