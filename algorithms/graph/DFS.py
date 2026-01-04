graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1],
    5: [2],
    6: [3],
    7: [3]
}
visited = []


def dfs(cur_v):
    #시작 node를 방문 리스트에 추가
    visited.append(cur_v)

    #인접한 node 순회하면 방문
    for v in graph[cur_v]:
        #각 node별 인접한 node 방문
        if v not in visited:
            #재귀로 방문 처리
            dfs(v)

    return visited

print(dfs(1))