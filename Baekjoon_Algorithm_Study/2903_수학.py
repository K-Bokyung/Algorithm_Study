# https://www.acmicpc.net/problem/2903

# 1. 입력값 받기
import sys

N = int(sys.stdin.readline())

# 2. 한 변의 점은 과정을 거칠 때마다 i+(i-1)개가 된다는 규칙을 반영해서 N번 이후 점의 수를 구하는 함수 작성
result = 0
dot = 2

for i in range(0, N):
  dot += (dot-1)

result = dot**2

print(result)