# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        if flowerbed == [0]:
            flowerbed = [1]
            n -= 1
        
        if flowerbed[-2:] == [0, 0]:
            flowerbed[-2:] = [0, 1]
            n -= 1
        
        if flowerbed[:2] == [0, 0]:
            flowerbed[:2] == [1, 0]
            n -= 1
        
        for i in range(len(flowerbed[1:-3])):
            if flowerbed[i+1:i+4] == [0, 0, 0]:
                flowerbed[i+1:i+4] = [0, 1, 0]
                n -= 1
                
        return n <= 0
