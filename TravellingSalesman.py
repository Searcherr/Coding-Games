import math
import numpy as np
from itertools import permutations
from sys import maxsize


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


def TSP_graph(graph, root_node_number):
    # making a list of nodes' indexes apart from root node
    vertex = []
    for i in range(n):
        if i != root_node_number:
            vertex.append(i)

    # storing min distance and min path
    min_distance = maxsize
    min_path = [root_node_number] + vertex + [root_node_number]
    # storing brute force
    next_permutation = permutations(vertex)
    for i in next_permutation:

        current_distance = 0
        current_path = [root_node_number]
        # compute current path distance
        k = root_node_number
        for j in i:
            # adding distance to the next node
            current_distance += graph[k][j]
            # moving column index to row's index
            k = j
            # adding the index of current point to the current path
            current_path.append(j)
        # adding the road home
        current_distance += graph[k][root_node_number]
        current_path.append(root_node_number)

        # updating minimum distance and it's path
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = current_path


    return min_distance, min_path


n = int(input('Enter the number of nodes: '))
nodes_array = np.zeros(shape=(n, 2))
for i in range(n):
    # x: The x coordinate of the given node
    # y: The y coordinate of the given node
    x, y = [int(j) for j in input().split()]
    nodes_array[i] = [x, y]

print(nodes_array)

user_graph = create_graph(nodes_array)
print(f"Your graph: \n {user_graph}")

starting_node_index = 0
result_distance = TSP_graph(user_graph, starting_node_index)[0]
result_path = TSP_graph(user_graph, starting_node_index)[1]
print(f"TSP distance = {result_distance}")
print(f"TSP path = {result_path}")

"""
test_graph = np.array([[1, 1],
                       [2, 2],
                       [3, 3],
                       [1, 1]])
test_result = calculate_distance(test_graph)
print(f"Test graph distance = {test_result}")
"""
