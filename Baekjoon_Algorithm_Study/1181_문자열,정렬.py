# https://www.acmicpc.net/problem/1181

# 1. 입력값 받기
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
words = [str(sys.stdin.readline().rstrip()) for _ in range(N)]

# 2. 중복된 단어는 제거하면서 길이 기준으로 리스트에 저장
max_word = len(max(words, key=lambda x : len(x)))
result = [[] for _ in range(max_word+1)]

for i in range(N):
  if words[i] not in result[len(words[i])]:
    result[len(words[i])].append(words[i])

# 3. 길이 순서대로 출력하면서 value가 여러 개면 사전 순으로 정렬해서 출력
for i in range(max_word+1):
  if len(result[i]) == 1:
    print(*result[i])
  elif len(result[i]) > 1:
    result[i].sort()
    for i in result[i]:
      print(i)
  else:
    continue