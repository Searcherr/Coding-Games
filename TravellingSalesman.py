import math
import numpy as np
from itertools import permutations
from sys import maxsize

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.




# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# You have to output a valid path



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
            graph[i, j] = calculate_distance(np.array([nodes_list[i], nodes_list[j]]))
    return graph


def swap_nodes_in_array(nodes_list, i, j):
    nodes_list[i], nodes_list[j] = nodes_list[j], nodes_list[i]
    return nodes_list[i], nodes_list[j]


def number_of_roads(number_of_nodes):
    return math.factorial(number_of_nodes - 1)


def travellingSalesmanProblem(graph, root_node_number):
    # making a list of nodes' indexes apart from root node
    vertex = []
    for i in range(n):
        if i != root_node_number:
            vertex.append(i)

    # storing min distance
    min_path = maxsize
    # storing brute force
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = root_node_number
        for j in i:
            current_pathweight += graph[k][j]

            k = j
        current_pathweight += graph[k][root_node_number]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path


n = int(input('Enter the number of nodes: '))  # This variables stores how many nodes are given
nodes_array = np.zeros(shape=(n, 2))
for i in range(n):
    # x: The x coordinate of the given node
    # y: The y coordinate of the given node
    x, y = [int(j) for j in input().split()]
    nodes_array[i] = [x, y]

print(nodes_array)

nodes_array_distance = calculate_distance(nodes_array)
record_distance = nodes_array_distance

temp = permutations(nodes_array)
print(temp)

"""
for _ in range(number_of_roads(n)):
    swap_nodes_in_array()
"""
users_graph = create_graph(nodes_array)

print(f"Your graph: \n {users_graph}")
print(f"Distance = {nodes_array_distance}")

starting_node_index = 0
resulr_distance = travellingSalesmanProblem(users_graph, starting_node_index)
print(f"TSP distance = {resulr_distance}")

test_graph = np.array([[1, 1],
                       [2, 2],
                       [3, 3],
                       [1, 1]])
test_result = calculate_distance(test_graph)
print(f"Test graph distance = {test_result}")
