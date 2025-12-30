from queue import PriorityQueue

pq = PriorityQueue()

#원소 삽입
pq.put(40)
pq.put(20)
pq.put(30)
pq.put(10)

#우선순위 큐 출력
print('우선순위 큐: ', pq.queue)
print(pq.queue)
print()

#최상위 원소 확인
removed_element = pq.get()
print('삭제된 원소: ', removed_element)
print('삭제 후 우선순위 큐: ', pq.queue)
print()