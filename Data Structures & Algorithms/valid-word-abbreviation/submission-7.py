class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        '''
        we are given a word and the abbr of that word
        and we are going to have one pointer go from the start
        of the first word and then the second word
        we must compare each character by character. check if the 
        character matches with the other and ofc if theres a different 
        character this becomes false and when we hit the digit we must 
        skip thse many characters 

        '''

        a, b = 0,0
        while a < len(word) and b < len(abbr): 
            if abbr[b] == '0':
                return False
            if word[a] == abbr[b]:
                a += 1
                b += 1
            elif abbr[b].isalpha():
                return False
            else: 
                sumLen = 0
                while b < len(abbr) and abbr[b].isdigit():
                    sumLen = sumLen * 10 + int(abbr[b])
                    b += 1 
                a += sumLen
        return a == len(word) and b == len(abbr)
