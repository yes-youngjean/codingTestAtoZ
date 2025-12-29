def sum_func(n):
    if n == 1:
        return 1
    return sum_func(n-1) + n

print(sum_func(3))

#재귀 함수를 종료하는 Base Case(기본 케이스)가 있어야 함