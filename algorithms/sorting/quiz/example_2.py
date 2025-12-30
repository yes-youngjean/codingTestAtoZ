# 개수
N = int(input())

lst = [input() for _ in range(N)] #N번 만큼 반복해서 문자열을 받음
reversed_lst = sorted(lst)

for word in reversed_lst:
    print(word)