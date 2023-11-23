# https://www.acmicpc.net/problem/27433

N = int(input())

def recursion(num):
    if num == 0:
        return 1
    result = recursion(num - 1)
    return num * result

print(recursion(N))
