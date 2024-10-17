# https://www.acmicpc.net/problem/2164

# 1
from collections import deque

n = int(input())
n_list = deque([x for x in range(1, n + 1)])

while len(n_list) > 1:
    n_list.popleft()
    n_list.append(n_list.popleft())

print(n_list[0])

# 2
import sys
from collections import deque

N = int(sys.stdin.readline())
n_list = deque(i for i in range(1, N+1))

while len(n_list) != 1:
    n_list.popleft()
    n_list.append(n_list.popleft())

print(*n_list)
