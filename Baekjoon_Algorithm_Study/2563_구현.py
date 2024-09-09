# https://www.acmicpc.net/problem/2563

# 1. 입력값 받기
import sys

p = int(sys.stdin.readline())
lo = [list(map(int, sys.stdin.readline().split())) for _ in range(p)]

# 2. 흰색 도화지는 10x10의 이중 리스트로 생성
wp = []

for _ in range(101):
  wp.append([0]*101)

# 3. 색종이의 위치를 찾아 그 부분은 1로 바꿈
for i in range(p):
  a, b = lo[i]
  c = 100-b
  for i in range(c-10, c):
    for j in range(a, a+10):
      wp[i][j] = 1

# 4. 1의 갯수를 구해서 넓이 출력
result = 0

for i in range(101):
  num = list.count(wp[i], 1)
  result += num
  
print(result)