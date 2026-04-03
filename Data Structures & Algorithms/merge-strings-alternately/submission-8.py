class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = [] 
        i, j = 0, 0
        length1, length2 = len(word1), len(word2)

        while i < length1 and j < length2:
            if i < length1: 
                result.append(word1[i])
            if j < length1:
                result.append(word2[j])
            i+=1
            j+=1
        while i < length1:
            result.append(word1[i])
            i += 1
        while j < length2:
            result.append(word2[j])
            j += 1
        return "".join(result)
        


