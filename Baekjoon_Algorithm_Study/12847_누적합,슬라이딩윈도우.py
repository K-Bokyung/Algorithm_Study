# https://www.acmicpc.net/problem/12847

import sys
N, M = [int(i) for i in sys.stdin.readline().split()]
money = [int(i) for i in sys.stdin.readline().split()]

start = 0
sum = sum(money[:M])
result = sum

while M < N:
    sum += money[M] - money[start]
    result = max(result, sum)
    start += 1
    M += 1
    
print(result)
