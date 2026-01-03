# 문제: 1000-N원에 대해 거스름돈의 최소 개수를 구하는 문제

N= int(input())
tg = 1000 - N

#거스름돈 개수
cnt = 0

#500
cnt = tg // 500
money = tg % 500

#100
cnt = cnt + money // 100
money = money % 100

#50
cnt = cnt + money // 50
money = money % 50

#10
cnt = cnt + money // 10
money = money % 10

#5
cnt = cnt + money // 5
money = money % 5

#1
cnt = cnt + money // 1
money = money % 1

print(cnt)

