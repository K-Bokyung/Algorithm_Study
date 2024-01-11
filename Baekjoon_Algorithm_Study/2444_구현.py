# https://www.acmicpc.net/problem/2444

star = int(input())
i = 1

while i < star + 1:
    print(" " * (star - i) + "*" * (2 * i - 1))
    i += 1

i = 1

while i < star:
    print(" " * i + "*" * ((2 * star - 1) - (2 * i)))
    i += 1
