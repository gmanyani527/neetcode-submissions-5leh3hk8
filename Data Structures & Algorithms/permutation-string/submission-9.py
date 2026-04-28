class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        count2 = {}
        
        for left in range(len(s1)):
            left_char = s1[left]

            if left_char in count1: 
                count1[left_char] += 1
            else: 
                count1[left_char] = 1
        
        left = 0

        for right in range(len(s2)):
            right_char = s2[right]
            if right_char in count2: 
                count2[right_char] += 1
            else: 
                count2[right_char] = 1
            while right - left + 1 > len(s1):
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1
            if count1 == count2:
                return True
        return False
                


        