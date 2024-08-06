# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missing_number(self, nums: list[int]) -> int:
        result = 0
        length = len(nums)
        total = sum([i for i in range(0, length + 1)])
        result = total - sum(nums)
        return result
