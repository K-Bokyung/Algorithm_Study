# https://www.acmicpc.net/problem/2751

# 1. 입력값 받기
import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# 2. 오름차순으로 정렬
nums.sort()

# 3. 결과를 한 줄에 하나씩 출력
for i in nums:
  print(i)