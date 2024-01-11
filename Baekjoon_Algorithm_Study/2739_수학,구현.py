# https://www.acmicpc.net/problem/2739

# 1
n = int(input())
answer = 0

for i in range(1, 10):
    answer = n * i
    print(n, '*', i, '=', answer, end= ' ')

# 2
n = int(input())

for i in range(1, 10):
    print(f'{i} * {i} = {n * i}')
