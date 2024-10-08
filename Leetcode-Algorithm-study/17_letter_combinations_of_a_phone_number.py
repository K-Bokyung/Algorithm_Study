# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letter_combinations(self, digits: str) -> list[str]:
        letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        result = []
        
        if digits == "":
            return result
        
        stack = [""]
        
        while stack:
            word = stack.pop()
            if len(word) == len(digits):
                result.append(word)
            if len(word) < len(digits):
                for i in letter_dict[digits[len(word)]]:
                    stack.append(word + i)

        return result