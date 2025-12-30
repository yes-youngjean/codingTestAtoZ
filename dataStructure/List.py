#리스트 선언
lst = [100, 200]

#맨 뒤에 원소 추가
lst.append(300)
print('원소 추가 후 lst: ', lst)
print()

#특정 index 원소 삭제
deleted_value = lst.pop(1)
print('삭제된 원소: ', deleted_value)
print('삭제 후 lst: ', lst)
print()

#맨 뒤 원소 삭제
deleted_value = lst.pop()
print('삭제된 원소: ', deleted_value)
print('삭제 후 lst: ', lst)
print()
lst.append(200)
lst.append(300)
lst.append(400)

#특정 위치 원소 접근 by index
print('인덱스 1의 원소: ', lst[1])
print()

#리스트의 크기 확인
print('리스트의 크기: ', len(lst))
print()

#특정 값의 존재 여부
value1 = 200
value2 = 700
print(value1 in lst)
print(value2 in lst)