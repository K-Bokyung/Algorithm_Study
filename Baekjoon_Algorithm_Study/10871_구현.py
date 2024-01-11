# https://www.acmicpc.net/problem/10871

# 1
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n) :
    if a[i] < x :
        print(a[i], end=' ')

# 2
N, X = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
bigger = []

for i in range(N):
    if a[i] < X:
        bigger.append(a[i])

print(*bigger)
