#sorted()함수의 key 옵션

def comp(x):
    return -x

arr1 = [4, 2, 3, 1, 5]
print(sorted(arr1))
print(sorted(arr1, key=comp))           # comp 함수를 썼을 때의 값을 기준으로 정렬하라!
print()
print(sorted(arr1, key=lambda x:x))     # Key 옵션의 기본값은 lambda x:x이다.+
print()



#cf) 람다
def func1(x, y):
    return x + y


func2 = lambda x, y : x + y
print(func1(1,2))
print(func2(1,2))