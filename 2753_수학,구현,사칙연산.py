# https://www.acmicpc.net/problem/2753

# 1
n = int(input())

if n % 100 == 0 and n % 400 != 0 :
    print(0)
elif n % 4 == 0 or n % 400 == 0 :
    print(1)
else :
    print(0)

# 2
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)
