# https://www.acmicpc.net/problem/1927

import sys
import heapq
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, X)