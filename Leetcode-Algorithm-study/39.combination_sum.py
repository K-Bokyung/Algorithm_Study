# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        result = []
        def dfs(idx, target):
            if target < 0:
                return
            elif target == 0:
                results.append(result[:])
                return
            for i in range(idx, len(candidates)):
                result.append(candidates[i])
                new_target = target - candidates[i]
                dfs(i, new_target)
                result.pop()
        dfs(0, target)
        return results
