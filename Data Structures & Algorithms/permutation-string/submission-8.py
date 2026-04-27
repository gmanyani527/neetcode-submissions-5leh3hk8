class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        count2 = {} 

        for char in s1:
            if char in count1:
                count1[char] += 1
            else: 
                count1[char] = 1
        
        left = 0 

        for char in range(len(s2)):
            right = s2[char]
            if right in count2:
                count2[right] += 1
            else: 
                count2[right] = 1
            
            if (char - left + 1) > len(s1):
                left_char = s2[left] 
                count2[left_char] -= 1
                if count2[left_char] == 0:
                    del count2[left_char]
                left += 1
            if count1 == count2:
                return True
        return False