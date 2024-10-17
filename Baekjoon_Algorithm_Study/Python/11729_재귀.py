# https://www.acmicpc.net/problem/11729

def hanoi(k, start, mid, end):
    if k == 1:
        print(start, end)
        return 1
    first = hanoi(k-1, start, end, mid)
    print(start, end)
    second = 1
    third = hanoi(k-1, mid, start, end)
    return

n = int(input())
print(2**n-1)
hanoi(n, 1, 2, 3)
