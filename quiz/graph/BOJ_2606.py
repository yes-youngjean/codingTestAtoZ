# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
#
# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
#
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

from collections import deque

M = int(input()) # 컴퓨터 개수
N = int(input()) # 간선 개수

# 그래프 초기화
graph = {i: [] for i in range(1, M+1)}

# 노드-노드 간선으로 연결
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

### ------

visited = []

def dfs(cur_v):
    visited.append(cur_v)

    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)

    return len(visited)-1


def bfs(graph, start_v):
    visited = [start_v]
    queue = deque([start_v])

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

    return len(visited)-1

print('bfs: ', bfs(graph, 1))
print('dfs: ', dfs(1))