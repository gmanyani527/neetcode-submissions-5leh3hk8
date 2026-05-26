class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1 = {}
        count2 = {} 

        for char in s:
            if char in count1:
                count1[char] += 1
            else: 
                count1[char] = 1
        for character in t: 
            if character in count2:
                count2[character] += 1
            else: 
                count2[character] = 1 
        if count1 == count2: 
            return True
        else:
            return False