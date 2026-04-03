class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1 = {}
        count2 = {} 

        for i in range(len(s)):
            if s[i] in count1:
                count1[s[i]] += 1
            else: 
                count1[s[i]] = 1
        for j in range(len(t)):
            if t[j] in count2:
                count2[t[j]] += 1
            else: 
                count2[t[j]] = 1
        return count1 == count2 