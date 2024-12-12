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
def bfs_with_prev(graph, start_node):
    """
    Perform BFS on a graph and save the previous node for each visited node.

    Args:
    - graph (dict): A dictionary where keys are nodes and values are lists of adjacent nodes.
    - start_node: The node from which BFS starts.

    Returns:
    - prev (dict): A dictionary where keys are nodes and values are their previous nodes.
    """
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Use a queue to manage the BFS process
    prev = {start_node: set()}  # Store the previous node (None for the start node)

    while queue:
        # Dequeue a node
        current_node = queue.popleft()

        # Process neighbors
        for neighbor in get_neighbors(graph, current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if neighbor not in prev:
                    prev[neighbor] = set()
                prev[neighbor].add(current_node)  # Save the previous node
            if neighbor in visited and current_node not in prev[neighbor]:
                prev[neighbor].add(current_node)
    
    return prev
def print_path(prev, start_node, target_node):
    """
    Print the path from the start_node to the target_node using backtracking.

    Args:
    - prev (dict): A dictionary where keys are nodes and values are their previous nodes (from BFS).
    - start_node: The node where the path starts.
    - target_node: The node where the path ends.

    Returns:
    - path (list): A list of nodes representing the path from start_node to target_node.
    """
    path = []
    current_node = target_node

    # Backtrack from target_node to start_node
    while current_node is not None:
        path.append(current_node)
        current_node = prev.get(current_node)

    # Check if the target_node is reachable from start_node
    if path[-1] != start_node:
        print(f"No path found from {start_node} to {target_node}.")
        return []

    # Reverse the path to get the correct order
    path.reverse()
    print(f"Path from {start_node} to {target_node}: {' -> '.join(path)}")
    return path

def filter_nine(matrix, lst):
    return [e for e in lst if matrix[e[0]][e[1]] == 9]
def filer_value(matrix, lst):
    return [matrix[e[0]][e[1]] for e in lst]
def print_path(prev, target_node):
    def helper(prev, node):
        if len(prev[node]) == 0:
            return 1
        sum_score = 0
        for prev_node in prev[node]:
            sum_score += helper(prev, prev_node)
        return sum_score
    return helper(prev, target_node) #node = 9

matrix = []
for line in sys.stdin:
    row = list(line)[:-1]
    row = [int(e) for e in row]
    matrix.append(row)
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            prev = bfs_with_prev(matrix, (i, j))
            nines = [e for e in prev if matrix[e[0]][e[1]] == 9]
            for nine in nines:
                count += print_path(prev, nine)
print(count)
            
