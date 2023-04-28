from collections import deque


def bfs(graph, start, goal):
    """
    The bfs function takes a graph, start node and goal node as input.
    It returns the shortest path from the start to goal nodes using breadth-first search.


    :param graph: Store the graph
    :param start: Specify the starting node
    :param goal: Specify the goal node
    :return: A list of nodes that is the shortest path from start to goal
    :doc-author: Rabii Elbeji
    """

    # keep track of visited nodes
    visited = set()

    # keep track of nodes to visit
    queue = deque()
    queue.append((start, [start]))

    while queue:
        (current, path) = queue.popleft()
        visited.add(current)

        # check if current node is goal node
        if current == goal:
            return path

        # queue up all unvisited neighbours of current node
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    # return None if there is no path
    return None


# test code
graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}

start = 'A'
goal = 'G'

path = bfs(graph, start, goal)

if path:
    print(f"Shortest path from {start} to {goal}: {' -> '.join(path)}")
else:
    print(f"No path found from {start} to {goal}")
