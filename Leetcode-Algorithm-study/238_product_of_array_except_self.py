# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        answer = 1
        for i in range(len(nums)-1):
            answer *= nums[i]
            result[i + 1] *= answer
        
        answer = 1
        for i in range(len(nums)-1, 0, -1):
            answer *= nums[i]
            result[i - 1] *= answer
        
        return result
