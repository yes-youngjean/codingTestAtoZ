#해시 테이블?
#=> 키와 값으로 이루어진 자료 구조
dt = dict()

dt['banana'] = 500
dt['apple'] = 700
dt['pear'] = 100

print('딕셔너리: ', dt)
print()
print('banana의 값: ', dt['banana'])
print()
del dt['banana']
print('banana 삭제 후: ', dt)
print()
print('딕셔너리 크기: ', len(dt))
print()
print('특정 키 존재 확인: ', 'apple' in dt)