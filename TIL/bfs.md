# 🚀 BFS (Breadth-First Search) 알고리즘 구현

Python을 사용한 **너비 우선 탐색(BFS)**의 기본적인 구현 방법을 기록한다.

---

## 1. 개요
**BFS**는 그래프 탐색 알고리즘으로, 시작 노드에서 가까운 노드부터 우선적으로 탐색하는 방식이다.

* **주요 용도:** 최단 경로 찾기, 임의의 경로 찾기, 네트워크 분석 등
* **자료구조:** 큐(Queue)를 사용하여 구현 (FIFO 방식)

---

## 2. 구현 코드 (Python)



```python
from collections import deque

def bfs(graph, start_v):
    """
    BFS 탐색 함수
    :param graph: dict 형태의 인접 리스트
    :param start_v: 시작 노드 번호
    :return: 방문한 순서대로의 리스트
    """
    # 1. 방문 여부를 기록할 리스트 (시작 노드 방문 처리)
    visited = [start_v]
    
    # 2. 탐색을 위한 큐 생성 (시작 노드 삽입)
    # 리스트를 deque로 감싸서 초기화한다
    queue = deque([start_v])

    # 3. 큐가 빌 때까지 반복
    while queue:
        # 큐의 맨 앞 요소를 추출
        cur_v = queue.popleft()
        
        # 현재 노드와 연결된 인접 노드 확인
        for v in graph[cur_v]:
            if v not in visited:        # 만약 아직 방문하지 않은 곳이면
                visited.append(v)       # 방문 처리하고
                queue.append(v)         # 인접 노드 방문하도록 큐에 넣기
                
    return visited

# --- 테스트를 위한 예시 그래프 ---
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1],
    5: [2],
    6: [3],
    7: [3]
}

print(f"방문 순서: {bfs(graph, 1)}")