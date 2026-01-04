from collections import deque

N, M = map(int, input().split())
graph = []

#그래프 완성
for _ in range(N):
    graph.append(list(map(int, input())))


#bfs 시작
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    #deque에 값이 있으면
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y]+1

    return graph[N-1][M-1]

print(bfs(0,0))
