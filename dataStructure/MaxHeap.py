from queue import PriorityQueue

#원소 삽입
pq = PriorityQueue()
pq.put([-40, 40])
pq.put([-30, 30])
pq.put([-20, 20])
pq.put([-10, 10])
print(pq.queue)
print()

#우선순위 큐 출력
removed_element = pq.get()
print('삭제된 원소: ', removed_element)
print('실제 사용할 값: ', removed_element[1])
print('삭제 후 우선순위 큐: ', pq.queue)