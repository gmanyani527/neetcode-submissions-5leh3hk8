class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1, length2 = len(word1), len(word2)
        a, b = 0,0
        result = []

        while a < length1 or b < length2: 
            if length1 > a: 
                result.append(word1[a])
            if length2 > b: 
                result.append(word2[b])
            a += 1 
            b += 1 
        return "".join(result)
