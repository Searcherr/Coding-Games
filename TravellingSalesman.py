import sys
import math
import numpy as np
from itertools import permutations

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
print(nodes_array)


def calculate_distance(nodes_list):
    total_distance = 0
    for i in range(len(nodes_list)-1):
        current_distance = math.sqrt(
            (nodes_list[i][0] - nodes_list[i+1][0]) ** 2 + ((nodes_list[i][1] - nodes_list[i+1][1]) ** 2)
        )
        total_distance += current_distance
    return total_distance


def create_graph(nodes_list):
    graph = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            #print(np.array([nodes_list[i], nodes_list[j]]))
            graph[i, j] = calculate_distance(np.array([nodes_list[i], nodes_list[j]]))
    return graph


def swap_nodes_in_array(nodes_list, i, j):
    nodes_list[i], nodes_list[j] = nodes_list[j], nodes_list[i]
    return nodes_list[i], nodes_list[j]


def number_of_roads(number_of_nodes):
    return math.factorial(number_of_nodes - 1)

nodes_array_distance = calculate_distance(nodes_array)
record_distance = nodes_array_distance

temp = permutations(nodes_array)
print(temp)

"""
for _ in range(number_of_roads(n)):
    swap_nodes_in_array()
"""

print(f"Your graph: \n {create_graph(nodes_array)}")
print(f"Distance = {nodes_array_distance}")

