# https://www.acmicpc.net/problem/9506

import sys

while True:
  n = int(sys.stdin.readline())
  
  # 1. -1이 나올 때까지 입력값 받기
  if n == -1:
    break
  
  #.2. n의 약수 구하기
  factors = []
  result = 0
  
  for i in range(1, n+1):
    if i != n and n % i == 0:
      factors.append(i)
      result += i
    
    if i == n and result != n:
      print(f'{n} is NOT perfect.')
    elif i == n and result == n:
      total = ''
      for i in range(len(factors)):
        if i == len(factors) -1:
          total += str(factors[i])
          break
        total += str(factors[i]) + ' + '
      print(f'{n} = {total}')