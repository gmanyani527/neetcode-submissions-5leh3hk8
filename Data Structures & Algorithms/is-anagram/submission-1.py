class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        window1 = {}
        window2 = {}

        for char in s: 
            if char in window1: 
                window1[char] += 1
            else: 
                window1[char] = 1
        for kar in t: 
            if kar in window2: 
                window2[kar] += 1
            else: 
                window2[kar] = 1
        if window1 == window2:
            return True
        else:
            return False