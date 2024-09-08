# https://www.acmicpc.net/problem/10988


# 1. 입력값 받기
import sys

word = sys.stdin.readline().rstrip()
word_list = [word[i] for i in range(len(word))]

# 2. 입력값을 거꾸로 정렬해서 같은지 비교
p_word_list = [word[len(word)-i-1] for i in range(len(word))]

if word_list == p_word_list:
  print(1)
else:
  print(0)
