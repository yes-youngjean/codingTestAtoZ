from collections import deque

#Stack => deque 이용
st = deque()

#맨 뒤 원소 추가
st.append(10)
st.append(20)
st.append(30)
print('st: ', st)
print()

removed_element = st.pop()
print('삭제된 원소: ', removed_element)
print('삭제 후 st: ', st)
print()

print('st가 비어있는지 확인: ', not st)

