# https://www.acmicpc.net/problem/5086

# 1. 입력값 받기
import sys

while True:
  A, B = map(int, sys.stdin.readline().split())
  
  # 2. while문을 break 하는 조건
  if A == 0 and B == 0:
    break
  
  # 3. 어떤 관계인지 구하는 if문
  if A < B and B % A == 0:
    print('factor')
  
  elif A > B and A % B == 0:
    print('multiple')
  
  else:
    print('neither') 
