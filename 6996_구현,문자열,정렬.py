# https://www.acmicpc.net/problem/6996

test = int(input())

for _ in range(test):
    n, m = [i for i in input().split()]
    if sorted(n) == sorted(m):
          print(n, "&", m, "are anagrams.")
    else:
          print(n, "&", m, "are NOT anagrams.")
