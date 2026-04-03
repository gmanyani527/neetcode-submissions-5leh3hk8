class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        length1, length2 = len(word), len(abbr)
        a, b = 0, 0

        while a < length1 and b < length2: 
            if abbr[b] == '0':
                return False
            if word[a] == abbr[b]:
                a += 1
                b += 1
            elif abbr[b].isalpha():
                return False
            else:
                sumLen = 0
                while b < length2 and abbr[b].isdigit():
                    sumLen = sumLen * 10 + int(abbr[b])
                    b += 1
                a += sumLen
        return a == length1 and b == length2