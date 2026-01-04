# 🚀 Dictionary Comprehension을 이용한 그래프 초기화

Python에서 그래프 알고리즘(DFS/BFS)을 풀 때, 인접 리스트를 가장 효율적으로 생성하는 방법을 기록한다.

---

## 1. 개요
**딕셔너리 컴프리헨션**은 반복 가능한 데이터로부터 새로운 딕셔너리를 빠르고 간결하게 생성하는 문법이다.

* **장점:** `for` 루프를 여러 줄 쓸 필요가 없어 가독성이 좋고, 속도가 빠르다.
* **특징:** 모든 정점을 키(Key)로 미리 등록해두어, 간선이 없는 고립 노드 탐색 시 발생할 수 있는 `KeyError`를 방지한다.

---

## 2. 구현 코드 (Python)



```python
# N: 정점의 개수, M: 간선의 개수, S: 시작 노드
N, M, S = map(int, input().split())

# 1. 딕셔너리 컴프리헨션으로 그래프 초기화
# {1: [], 2: [], ..., N: []} 형태가 생성됨
graph = {i: [] for i in range(1, N + 1)}

# 2. 간선 정보 입력 및 그래프 구성
for _ in range(M):
    u, v = map(int, input().split())
    # 양방향 그래프인 경우 양쪽에 추가
    graph[u].append(v)
    graph[v].append(u)

# 결과 확인
print(f"생성된 그래프: {graph}")