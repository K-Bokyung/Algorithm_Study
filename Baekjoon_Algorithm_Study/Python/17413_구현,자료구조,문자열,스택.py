# https://www.acmicpc.net/problem/17413

# 1. 입력값 받기
import sys

S = sys.stdin.readline().rstrip()

# 2. 띄어쓰기를 고려하며 태그 구별, 문자열은 뒤집기
S = S.replace(' ', '-')
result = []
word = []
tag_on = False

for i in range(len(S)):
  if S[i] == '-' and tag_on == True:
    result.append(S[i])
  elif S[i] == '-' and tag_on == False:
    s = ''.join(reversed(word))
    result.append(s)
    result.append(S[i])
    word = []
  elif S[i] == '<' and len(word) >= 1:
    s = ''.join(reversed(word))
    result.append(s)
    result.append(S[i])
    tag_on = True
    word = []
  elif S[i] == '<' and len(word) == 0:
    result.append(S[i])
    tag_on = True
  elif S[i] == '>':
    result.append(S[i])
    tag_on = False
  elif tag_on == False and i == len(S) -1:
    word.append(S[i])
    s = ''.join(reversed(word))
    result.append(s)
  elif tag_on == False and i != len(S) -1:
    word.append(S[i])
  elif tag_on == True:
    result.append(S[i])

result = ''.join(result).replace('-', ' ')
print(result)