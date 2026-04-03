class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        length1, length2 = len(word), len(abbr)
        i, j = 0, 0

        while i < length1 and j < length2: 
            if abbr[j] == '0':
                return False 
            if word[i] == abbr[j]: 
                i += 1 
                j += 1 
            elif abbr[j].isalpha():
                return False
            else: 
                sumlen = 0
                while j < length2 and abbr[j].isdigit():
                    sumlen = sumlen * 10 + int(abbr[j])
                    j += 1
                i += sumlen
        return i == length1 and j == length2