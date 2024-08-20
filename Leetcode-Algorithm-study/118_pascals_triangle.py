# https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle_list = [[0]*(i+1) for i in range(numRows)]
        
        for i in range(len(triangle_list)):
            triangle_list[i][0] = 1
            triangle_list[i][-1] = 1
        
        for i in range(2, numRows):
            for j in range(1, i):
                triangle_list[i][j] = triangle_list[i-1][j-1] + triangle_list[i-1][j]

        return triangle_list