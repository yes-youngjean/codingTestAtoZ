from collections import deque


N, M, S = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

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


visited_dfs = []

def dfs(cur_v):
    visited_dfs.append(cur_v)

    for v in graph[cur_v]:
        if v not in visited_dfs:
            dfs(v)

    return visited_dfs

print(dfs(S))
print(bfs(graph, S))
