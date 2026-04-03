class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        '''
        we are given two words and we must check if 
        they even fit each other

        constraints i can notice is that there cannot be zeros 

        best to have two pointer one for each word and traverse
        forward    

        '''

        i, j = 0, 0
        length1, length2 = len(word), len(abbr)


        while i < length1 and j < length2:
            if abbr[j] == "0":
                return False
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha():
                return False
            else: 
                sumLen = 0
                while j < length2 and abbr[j].isdigit(): 
                    sumLen = sumLen * 10 + int(abbr[j])
                    j+=1
                i += sumLen
        return i == length1 and j == length2