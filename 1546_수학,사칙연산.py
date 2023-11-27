# https://www.acmicpc.net/problem/1546

# 1
n = int(input())
l = list(map(int, input().split()))
l.sort()
m = l[n-1]
a = 0
result = 0

for i in range(n) :
    l[i] = l[i]/m * 100
    a += l[i]

result = a/n
print(result)

# 2
import sys

N = int(sys.stdin.readline())
score_list = [int(i) for i in sys.stdin.readline().split()]
score = sum([score_list[i]/max(score_list)*100 for i in range(N)]) / N
print(score)
