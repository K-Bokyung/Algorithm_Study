# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        min_count = len(blocks)
        
        for i in range(len(blocks)-k+1):
            new_count = blocks[i:i+k].count('W')
            min_count = min(min_count, new_count)
        
        return min_count