# https://leetcode.com/problems/largest-number/description/

class Solution:
    def largest_number(self, nums: list[int]) -> str:
        nums = [str(i) for i in nums]        
        nums.sort(key=lambda x:(x*9), reverse=True)
        return str(int(''.join(nums)))
