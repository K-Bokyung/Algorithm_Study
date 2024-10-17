# https://www.acmicpc.net/problem/10808

# 1. 입력값 받기
import sys
from collections import defaultdict

S = sys.stdin.readline().rstrip()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s_dict = defaultdict(int)

# 2. 단어 S의 알파벳 갯수를 딕셔너리 형식으로 저장
for i in alpha:
  s_dict[i] = 0

for i in S:
  s_dict[i] += 1

# 3. 딕셔너리 값만 출력
result = s_dict.values()
print(*result)