class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        a,b = 0, 0
        result = [] 

        while a < length1 or b < length2: 
            if a < length1: 
                result.append(word1[a])
            if b < length2: 
                result.append(word2[b])
            a += 1
            b += 1 
            
        return ''.join(result)