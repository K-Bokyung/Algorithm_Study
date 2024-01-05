# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
          ")":"(",
          "}":"{",
          "]":"["
        }
        
        for i in s:
            if i not in mapping:
                stack.append(i)
            elif not stack or mapping[i] != stack.pop():
                return False
        return bool(not stack)
