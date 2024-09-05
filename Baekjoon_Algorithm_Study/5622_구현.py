# https://www.acmicpc.net/problem/5622

# 1. 입력값 받기
import sys

phone_num = sys.stdin.readline().rstrip()

# 2. 숫자 별로 알파벳 분해서 리스트화
num_list = [1, [2, 'ABC'], [3, 'DEF'], [4, 'GHI'], [5, 'JKL'], [6, 'MNO'], [7, 'PQRS'], [8, 'TUV'], [9, 'WXYZ'], [0, 'OPERATOR']]

# 3. 단어에 따라 숫자를 찾고 거는 시간 구하기
time = 0

for i in phone_num:
  for j in range(1, len(num_list) - 1):
    if i in num_list[j][1]:
      time += (2 + j)

print(time)