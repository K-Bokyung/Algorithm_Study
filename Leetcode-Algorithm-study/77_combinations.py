# https://leetcode.com/problems/combinations/description/

import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [list(i) for i in itertools.combinations(range(1, n+1), k)]
        return result