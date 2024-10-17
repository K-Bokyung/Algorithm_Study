# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline())
meeting = []

for i in range(N):
    start, end = [int(i) for i in sys.stdin.readline().split()]
    meeting.append((start, end))

meeting.sort(key=lambda x:(x[1], x[0]))

result = 0
finish_time = 0

for i in meeting:
    start_time, end_time = i
    if start_time >= finish_time:
        result += 1
        finish_time = end_time
        
print(result)