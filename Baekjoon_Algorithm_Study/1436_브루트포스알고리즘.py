# https://www.acmicpc.net/problem/1436

# 1. 입력값 받기
import sys

N = int(sys.stdin.readline())

# 2. 6이 3개 이상 연속으로 들어가는 N번째로 작은 종말의 수 구하기
# 예시: 6번째로 작은 종말의 수는 5666
# 예시: 17번째로 작은 종말의 수는 16660 (추정)
# 예시: 187번째로 작은 종말의 수는 66666
# 예시: 500번째로 작은 종말의 수는 166699
# * 즉, 666이 들어가는 모든 수 중 N번째 수를 찾으면 된다.

results = []
str_n = str(N)
limit = str_n +'666'
limit_n = int(limit)

for i in range(666, limit_n):
  if '666' in str(i):
    results.append(i)
    
print(results[N-1])