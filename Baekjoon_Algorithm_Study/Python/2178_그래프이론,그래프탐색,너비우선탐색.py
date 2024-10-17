# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

n, m = [int(i) for i in sys.stdin.readline().split()]
maze = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]

visited = deque()
visited.append([0, 0])

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def maze_bfs():
    while visited:
        x, y = visited.popleft()
        for i in direction:
            go_x = x + i[0]
            go_y = y + i[1]
            if 0 <= go_x < m and 0 <= go_y < n:
                if maze[go_y][go_x] == 1:
                    maze[go_y][go_x] = maze[y][x] + 1
                    visited.append([go_x, go_y])
    maze[0][0] = 1

maze_bfs()
print(maze[n-1][m-1])