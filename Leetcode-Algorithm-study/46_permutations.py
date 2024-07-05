# https://leetcode.com/problems/permutations/description/

def permutation(nums: list[int]) -> list[list[int]]:
    result = []
    tem_result = []
    def per_dfs(nums):
        if len(nums) == 0:
            result.append(tem_result[:])
            return
            
        for i in nums:
            tem_result.append(i)
            tem_nums = nums[:]
            tem_nums.remove(i)
            per_dfs(tem_nums)
            tem_result.pop()
        
    per_dfs(nums)
    return result