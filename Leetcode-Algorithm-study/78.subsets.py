# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
            results=[]
            subset=[]
            index = 0
            def dfs(idx, subset):
                results.append(subset)
                for i in range(idx, len(nums)):
                    new_subset = subset[:]
                    new_subset.append(nums[i])
                    dfs(i+1, new_subset)
            dfs(index, subset)
            return(results)