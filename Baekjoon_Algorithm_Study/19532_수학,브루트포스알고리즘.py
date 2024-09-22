# https://www.acmicpc.net/problem/19532

# 1. 입력값 받기
import sys

a, b, c, d, e, f = list(map(int, sys.stdin.readline().split()))

# 2. 주어진 방정식 구현
x = 0
y = 0

(a * x) + (b * y) == c
(d * x) + (e * y) == f

# 3. for문으로 첫번째 방정식에 적합한 x, y를 구한 후 두번째 방정식에 적용
results = []

for i in range(-999, 1000):
  for j in range(-999, 1000):
    if (a * i) + (b * j) == c and (d * i) + (e * j) == f :
      results.append(i)
      results.append(j)

print(*results)
