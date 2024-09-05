# https://www.acmicpc.net/problem/9086

# 1. 입력값 받기
import sys

T = int(sys.stdin.readline())

# 2. 첫 글자와 마지막 글자 연속 출력
for i in range(T):
  word = sys.stdin.readline().rstrip()
  if len(word) == 0:
    print(word + word)
  else:
    print(word[0] + word[-1])