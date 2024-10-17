# https://www.acmicpc.net/problem/10807

# 1. 입력값 받기
import sys

n = int(sys.stdin.readline())
n_list = [int(i) for i in sys.stdin.readline().split()]
v = int(sys.stdin.readline())

# 2. n_list 중에 v가 몇 개인지 찾기
result = [i for i in n_list if i == v]

print(len(result))