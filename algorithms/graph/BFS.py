from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque([start_v])

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1],
    5: [2],
    6: [3],
    7: [3]
}

print(bfs(graph, 1))