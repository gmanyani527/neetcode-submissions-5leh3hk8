class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {} 
        count2 = {} 

        for i in range(len(s1)):
            char = s1[i]
            if char in count1:
                count1[char] += 1
            else: 
                count1[char] = 1
            
        left = 0
        for j in range(len(s2)):
            right_char = s2[j]
            if right_char in count2: 
                count2[right_char] += 1
            else: 
                count2[right_char] = 1
            while j - left + 1 > len(s1):
                left_char = s2[left]
                count2[left_char] -= 1
                if count2[left_char] == 0:
                    del count2[left_char]
                left += 1
            if count1 == count2:
                return True
        return False

            