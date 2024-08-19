# https://www.acmicpc.net/problem/1629

import sys

A, B, C = [int(i) for i in sys.stdin.readline().split()]

def calculate(a, b, c):
    if b == 1:
        return a % c
    else:
        result = calculate(a, b//2, c)
        if b % 2 == 0:
            return result * result % c
        else:
            return result * result * a % c

print(calculate(A, B, C))
