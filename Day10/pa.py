import sys
from collections import deque

def get_neighbors(graph, node):
    curr_score = graph[node[0]][node[1]]
    neighbors = []
    if node[1] + 1 < len(graph[0]) and graph[node[0]][node[1]+1] - curr_score == 1:
        neighbors.append((node[0], node[1]+1))
    if node[1] - 1 >= 0 and graph[node[0]][node[1]-1] - curr_score == 1:
        neighbors.append((node[0], node[1]-1))
    if node[0] + 1 < len(graph) and graph[node[0]+1][node[1]] - curr_score == 1 :
        neighbors.append((node[0]+1, node[1]))
    if  node[0] - 1 >= 0 and graph[node[0]-1][node[1]] - curr_score == 1:
        neighbors.append((node[0]-1, node[1]))
    return neighbors
def bfs(graph, start_node):
    """
    Perform BFS on a graph.

    Args:
    - graph (dict): A dictionary where keys are nodes and values are lists of adjacent nodes.
    - start_node: The node from which BFS starts.

    Returns:
    - visited_nodes (list): A list of nodes in the order they are visited.
    """
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Use a queue to manage the BFS process
    visited_nodes = []  # To record the order of visited nodes

    while queue:
        # Dequeue a node
        current_node = queue.popleft()

        # If not visited, process the node
        if current_node not in visited:
            visited.add(current_node)
            visited_nodes.append(current_node)

            # Enqueue all unvisited neighbors
            for neighbor in get_neighbors(graph, current_node):
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited_nodes

def filter_nine(matrix, lst):
    return [e for e in lst if matrix[e[0]][e[1]] == 9]
matrix = []
for line in sys.stdin:
    row = list(line)[:-1]
    row = [int(e) for e in row]
    matrix.append(row)
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            count += len(filter_nine(matrix, bfs(matrix, (i, j))))
            
print(count)