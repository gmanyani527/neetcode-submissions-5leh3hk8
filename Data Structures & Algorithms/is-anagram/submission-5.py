class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = {}
        set2 = {} 

        for char in s: 
            if char not in set1: 
                set1[char] = 0 
            else: 
                set1[char] += 1
        for char in t:
            if char not in set2:
                set2[char] = 0
            else:
                set2[char] += 1
        return set1 == set2