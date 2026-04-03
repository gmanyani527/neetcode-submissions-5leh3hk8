class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = 0
        b = 0
        result = []

        while a < len(word1) or b < len(word2):
            if a < len(word1): 
                result.append(word1[a])
                a += 1
            if b < len(word2): 
                result.append(word2[b])
                b += 1
        return "".join(result)