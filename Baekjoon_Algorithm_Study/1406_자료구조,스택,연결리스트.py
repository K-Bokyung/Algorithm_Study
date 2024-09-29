# https://www.acmicpc.net/problem/1406

# 1. 입력값 받기
import sys

n_word = sys.stdin.readline().rstrip().split()
n_word2 = []

M = int(sys.stdin.readline())
m_order = [sys.stdin.readline().rstrip().split() for _ in range(M)]

# 2. 명령어를 조건문으로 나누어 문자열 수정
for i in range(M):
  if m_order[i][0] == 'L' and len(n_word) > 0:
    n_word2.append(n_word.pop())
    
  elif m_order[i][0] == 'D' and len(n_word2) > 0:
    n_word.append(n_word2.pop())
    
  elif m_order[i][0] == 'B' and len(n_word) > 0:
    n_word.pop()
    
  elif m_order[i][0] == 'P':
    n_word.append(m_order[i][1])

# 3. 문자열 출력
n_word = ''.join(n_word)
n_word2 = ''.join(reversed(n_word2))

print(n_word + n_word2)

