# https://leetcode.com/problems/group-anagrams/description/

import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer = []
        an_dict = collections.defaultdict(list)
        
        for i in range(len(strs)):
            str = ''.join(sorted(strs[i]))
            if str not in an_dict:
                an_dict[str] = [strs[i]]
            else:
                an_dict[str].append(strs[i])
            
            answer = list(an_dict.values())
        
        return answer

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
result= sol.groupAnagrams(strs)

print(result)