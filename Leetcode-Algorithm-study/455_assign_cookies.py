# https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def find_content_children(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        
        for i in g:
            for j in s:
                if i <= j:
                    s.remove(j)
                    result += 1
                    break
        
        return result