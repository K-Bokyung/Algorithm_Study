# https://www.acmicpc.net/problem/2953

# 1
import sys

score_list = []
for i in range(5):
    score = [int(i) for i in sys.stdin.readline().split()]
    score_list.append(sum(score))

print(score_list.index(max(score_list)) + 1, max(score_list))

# 2
import sys

score = [[int(i) for i in sys.stdin.readline().split()] for _ in range(5)]
score_list = [sum(score[i]) for i in range(5)]

print(score_list.index(max(score_list)) + 1, max(score_list))
