# N개 숫자가 주어질 때, 숫자들을 오름차순으로 정렬한 결과와 내림차순으로 정렬한 결과를 출력하시오.
# -1, 3, 0, 7, 0, 10, -3, 7, 1, 8

#입력한 것들을 숫자로 바꿔서 List에 넣음
lst = list(map(int, input().split()))
print(lst)

test1 = ' '.join(map(str, sorted(lst)))
print(test1)

test2 = ' '.join(map(str, sorted(lst, reverse = True)))
print(test2)


###! join() 함수는 오직! 문자열로 된 iterable만 합칠 수 있다!!