# https://www.acmicpc.net/problem/10773

# 1
k = int(input())
k_list = []
result = 0

for _ in range(k):
    num = int(input())
    if num == 0:
        k_list.pop()
    else:
        k_list.append(num)

result = sum(k_list)
print(result)

# 2
import sys

K = int(sys.stdin.readline())
result = []

for _ in range(K):
    money = int(sys.stdin.readline())
    if money == 0:
        result.pop()
    else:
        result.append(money)

print(sum(result))
