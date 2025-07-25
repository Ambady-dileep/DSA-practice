from collections import deque
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])
graph = {
    'A': ['B'],
    'B': ['O', 'D'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
    'O': []
}
bfs(graph, 'A')