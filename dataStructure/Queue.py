from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)

print('큐: ', q)
print()

removed_element = q.popleft()
print('삭제된 원소: ', removed_element)
print('큐 출력: ', q)
print()