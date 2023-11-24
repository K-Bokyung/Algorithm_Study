# https://www.acmicpc.net/problem/1920

# 1
import sys

input = sys.stdin.readline
n = int(input())
n_set = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_set:
        print(1)
    else:
        print(0)
        
# 2
import sys

n = int(sys.stdin.readline())
n_set = set([int(i) for i in sys.stdin.readline().split()])
m = int(sys.stdin.readline())
m_list= [int(i) for i in sys.stdin.readline().split()]

for i in m_list:
    if i in n_set:
        print(1)
    else:
        print(0)