# https://www.acmicpc.net/problem/2941

# 1. 입력값 받기
import sys

word = sys.stdin.readline().rstrip()

# 2. 크로아티아 알파벳 찾아서 빈칸으로 대체
c_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c_word:
  word = word.replace(i, '!')

print(len(word))