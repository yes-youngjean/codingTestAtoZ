N = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2, reverse = True)


sum = 0
# for i in arr1_asc:
#     for j in arr2_desc:
#         sum = sum + (i * j)
# => 이러면 다 순회함;;

for i in range(N):
    sum = sum + arr1[i] * arr2[i]

print(sum)


