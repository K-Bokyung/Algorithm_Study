# https://www.acmicpc.net/problem/1316

# 1. 입력값 받기
import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

# 2. 그룹 단어가 아닌 것을 찾고 개수를 구하기
result = N

for i in words:
  word_list = []
  for j in range(len(i)):
    print('j', j)
    if i[j] not in word_list:
      word_list.append(i[j])
      print('1', word_list)
    elif i[j] in word_list and i[j-1] != i[j]:
      result -= 1
      print('result', result)
      print('2', word_list)
      break

if result < 0:
  result = 0

print(result)