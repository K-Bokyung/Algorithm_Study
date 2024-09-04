# https://www.acmicpc.net/problem/5597

# 1. 입력값 받기
import sys

students = [int(sys.stdin.readline()) for _ in range(28)]
result = []

# 2. 과제 안 낸 학생들을 result에 append
for i in range(1, 31):
  if i not in students:
    result.append(i)

# 3. 결과 출력
for i in result:
  print(i)