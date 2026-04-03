class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1, length2 = len(word1), len(word2)
        a,b = 0, 0
        rslt = []

        while a < length1 or b < length2: 
            if a < length1: 
                rslt.append(word1[a])
            if b < length2: 
                rslt.append(word2[b])
            a += 1
            b += 1 
        return ''.join(rslt)