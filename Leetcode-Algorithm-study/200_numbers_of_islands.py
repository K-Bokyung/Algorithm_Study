# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def num_islands(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] != '1':
                return
            
            grid[i][j] = '0'
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
                    
        return count