# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lt = i + 1
            rt = len(nums) - 1
            while lt < rt:
                temp_sum = nums[i] + nums[lt] + nums[rt]
                if temp_sum == 0:
                    result.append([nums[i], nums[lt], nums[rt]])
                    while lt < rt and nums[lt] == nums[lt+1]:
                        lt += 1
                    while lt <rt and nums[rt] == nums[rt-1]:
                        rt -= 1
                    lt += 1
                    rt -= 1
                elif 0 < temp_sum:
                    rt -= 1
                elif 0 > temp_sum:
                    lt += 1
        
        return result
