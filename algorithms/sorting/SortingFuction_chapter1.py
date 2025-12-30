#파이썬 정렬 함수
#=> sort(): List에서만 사용 가능
#=> sorted(): iterable 객체(순회할 수 있는 객체) 모두에서 사용 가능함 (리스트, 튜플, 셋, 딕셔너리, 문자열 등)
#=> List 형태로 반환함

lst = [3,4,5,1,2]
print(lst)
sorted_lst = sorted(lst)
print(sorted_lst)
print(type(sorted_lst))
print('------------------------------')


tp = (3,4,5,1,2)
print(tp)
sorted_tp = sorted(tp)
print(sorted_tp)
print(type(sorted_tp))
print('------------------------------')


dt = {'d':1, 'a':2, 'c':3}
print(dt)
print(list(dt))             #=> key만 가지고 List를 만든다
print(sorted(dt))           #=> key로만 배열을 만들고 오름차순 정렬
print(type(sorted(dt)))     #=> 타입: List
print('------------------------------')


st= "aonqknddf"
print(st)
print(list(st))
print(sorted(st))
print(type(sorted(st)))