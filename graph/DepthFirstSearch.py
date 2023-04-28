def dfs(graph, start, goal):
    """
    The dfs function takes a graph, start node and goal node as input.
    It returns the path from the start to goal nodes if there is one.
    If not, it returns None.

    :param graph: Pass in the graph that we want to search
    :param start: Specify the starting node
    :param goal: Specify the goal node
    :return: A list of nodes that are visited, in the order they were visited
    :doc-author: Rabii Elbeji
    """
    visited = set()
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))
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

path = dfs(graph, start, goal)

if path:
    print(f"Shortest path from {start} to {goal}: {' -> '.join(path)}")
else:
    print(f"No path found from {start} to {goal}")
