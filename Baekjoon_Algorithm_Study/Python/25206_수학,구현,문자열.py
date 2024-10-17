# https://www.acmicpc.net/problem/25206

# 1. 입력값 받기
import sys

score_list = [sys.stdin.readline().rstrip().split() for _ in range(20)]
step_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0': 2.0, 'D+':1.5, 'D0': 1.0, 'F':0.0}

# 2. 전공 평점 구하기 (등급이 P인 과목 제외)
step_sum = 0
grade_sum = 0
result = 0

for i in score_list:
  if i[2] != 'P':
    a = float(i[1])
    b = step_dict[i[2]]
    step_sum += (a * b)
    grade_sum += a

result = step_sum / grade_sum
print(format(result, ".6f"))