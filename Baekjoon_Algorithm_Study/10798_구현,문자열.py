# https://www.acmicpc.net/problem/10798

# 1. 입력값 받기
import sys
from collections import deque
from collections import defaultdict

words_list = [deque(sys.stdin.readline().rstrip()) for _ in range(5)]

# 2. 세로로 읽은 순서대로 글자들을 배치하기
words_dict = defaultdict(list)

for i in range(5):
  for j in range(len(words_list[i])):
      if len(words_list[i]) <= 0:
        break
      else:
        copy_list = words_list[i]
        words_dict[j].append(copy_list.popleft())
        words_list[i] = copy_list

# 3. 공백 없이 연속해서 출력
result = ''

for i in range(len(words_dict)):
  words_join = ''.join(words_dict[i])
  result += words_join

print(result)