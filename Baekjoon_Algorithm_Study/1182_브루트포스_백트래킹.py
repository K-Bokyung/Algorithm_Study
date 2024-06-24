# https://www.acmicpc.net/problem/1182

import sys

N, S = map(int, sys.stdin.readline().split())
arr = [int(i) for i in sys.stdin.readline().split()]
count = 0

def dfs(idx, sum):
    global count
    if idx >= N:
        return
    sum += arr[idx]
    if sum == S:
        count += 1
    dfs(idx + 1, sum)
    dfs(idx + 1, sum - arr[idx])
    
dfs(0, 0)
print(count)